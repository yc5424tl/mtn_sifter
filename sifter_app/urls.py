from django.urls import path

from . import views

urlpatterns = [
    path('/stay_alive', views.stay_alive, name='stay_alive'),
]