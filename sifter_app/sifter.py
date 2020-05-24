from .models import Source, Category
from .data import api_country_codes, categories, country_codes
from random import random
import os
import requests
from http import HTTPStatus
import logging
from django.templatetags.static import static
import json
import time
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events


logger = logging.getLogger(__name__)

api_key = os.getenv('SIFTER_API_KEY')

scheduler = BackgroundScheduler()
register_events(scheduler)


def sift():
    rand_country, rand_category = get_random_target()
    country_src_data = req_country_src_data(alpha2_code=rand_country, src_cat=rand_category)
    if country_src_data is not None:
        src_update = build_country_src_data(
            src_data=country_src_data,
            alpha2_code=rand_country,
            src_cat=rand_category
        )
        send_payload(src_update)


def send_all_src():
    if verify_base_cat() and verify_base_src():
        sources = Source.objects.all()
        src_update = set()
        for src in sources:
            src_update.add(src.json)
        return send_payload(src_update)


def verify_base_cat():
    for cat in categories:
        Category.objects.get_or_create(name=cat)
    return True


def verify_base_src():
    try:
        Source.objects.get(id=1)
    except (AttributeError, Source.DoesNotExist):
        src_update = set()
        try:
            with open(static('top_sources.json')) as json_data:
                src_data = json.load(json_data)['sources']
                for src in src_data:
                    cat = Category.objects.get_or_create(name=src['category'])
                    new_src = Source.objects.create(
                        name=src['name'],
                        country=src['country'],
                        language=src['language'],
                        url=src['url']
                    )
                    new_src.categories.add(cat)
                    new_src.save()
                    src_update.add(new_src.json)
                return send_payload(src_update)
        except FileNotFoundError:
            logger.log(level=logging.INFO, msg='Unable to locate file to build sources.')
            src_data = req_top_src_data()
            if src_data:
                src_update = build_top_src_data(src_data)
                if send_payload(src_update):
                    scheduler.pause()
                    time.sleep(360)
                    scheduler.resume()
                    return True
            return False


def send_payload(src_update: set):
    login_url = os.getenv('PAYLOAD_LOGIN')
    username = os.getenv('PAYLOAD_USER')
    password = os.getenv('PAYLOAD_PASS')
    post_url = os.getenv('PAYLOAD_POST')

    client = requests.session()
    client.get(login_url)
    csrf_token = client.cookies['csrftoken']

    login_data = {
        'username': username,
        'password': password,
        'csrfmiddlewaretoken': csrf_token,
        'next': '/'
    }

    payload = {'sources': frozenset(src_update)}
    try:
        r1 = client.post(login_url, data=login_data, headers=dict(Referer=login_url))
        logger.log(level=logging.INFO, msg=f'response_1 => {r1}')
        r2 = client.post(url=post_url, json=payload)
        logger.log(level=logging.INFO, msg=f'response_2 => {r2}')
        return True
    except ConnectionError:
        logger.log(level=logging.INFO, msg='ConnectionError during send_payload')
        return False
    except:
        return False


def get_random_target():
    countries = list(api_country_codes.keys())
    rand_country = random.choice(countries)
    rand_category = random.choice(categories)
    return rand_country, rand_category


def req_country_src_data(alpha2_code, src_cat=None):
    if src_cat is None:
        endpoint = f'https://newsapi.org/v2/top-headlines?country={alpha2_code}&apiKey={api_key}'
    else:
        endpoint = f'https://newsapi.org/v2/top-headlines?country={alpha2_code}&category={src_cat}&apiKey={api_key}'
    try:
        response = requests.get(endpoint)
        if response.status_code == HTTPStatus.OK:
            return response.json()['articles']
        else:
            response.raise_for_status()
            # log
            return None
    except requests.exceptions.HTTPError as err:
        return None


def build_country_src_data(src_data, alpha2_code, src_cat) -> set:
    src_update = set()
    cat, c_created = Category.objects.get_or_create(name=src_cat)
    for article in src_data:
        src = check_for_source(article['source']['name'])
        if src is None:
            new_src = Source.objects.create(
                name=article['source']['name'],
                country=alpha2_code,
                language=country_codes.get(alpha2_code).get('language')
            )
            new_src.categories.add(cat)
            new_src.save()
            src_update.add(new_src.json)
        else:
            if cat not in src.categories:
                src.categories.add(cat)
                src.save()
                src_update.add(src.json)
    return src_update


def req_top_src_data():
    response = requests.get(f'https://newsapi.org/v2/sources?apiKey={api_key}')
    try:
        if response.status_code == HTTPStatus.OK:
            return response.json()['articles']
        else:
            response.raise_for_status()
            # log
            return None
    except requests.exceptions.HTTPError as err:
        # log err
        return None


def build_top_src_data(src_data) -> set:
    src_update = set()
    for src in src_data:
        cat = Category.objects.get_or_create(name=src['category'])
        cat.save()
        source = check_for_source(src['name'])
        if source is None:
            new_src = Source.objects.create(
                name=src['name'],
                country=src['country'],
                language=src['language'],
                url=src['url']
            )
            new_src.categories.add(cat)
            new_src.save()
            src_update.add(new_src.json)
        else:
            if cat not in src.categories:
                src.categories.add(cat)
                src.save()
                src_update.add(src.json)
    return src_update


def check_for_source(src_name):
    if src_name:
        try:
            return Source.objects.get(name=src_name)
        except (AttributeError, Source.DoesNotExist) as err:
            logger.log(
                level=logging.ERROR,
                msg=f'{err} during sifter.check_for_source({src_name}'
            )
            return None
    else:
        # log
        return None


def start():
    scheduler.add_job(
        id='sift_scheduler',
        func=sift,
        trigger='interval',
        minutes=6,
        max_instances=1,
        replace_existing=True
    )

    if send_all_src():
        scheduler.start()
        logger.log(level=logging.INFO, msg='starting scheduler')
    else:
        logger.log(level=logging.CRITICAL, msg='Failed send all, scheduler not started.')
