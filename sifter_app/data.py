categories = [
    "business",
    "entertainment",
    "health",
    "science",
    "sports",
    "technology",
    "general",
]

api_country_codes = {
    "ar": {"name": "Argentina", "language": "es"},
    "au": {"name": "Australia", "language": "en"},
    "at": {"name": "Austria", "language": "de"},
    "be": {
        "name": "Belgium",
        "language": "nl",
    },  # 'nl' most likely followed by 'fr', some 'de'
    "br": {"name": "Brazil", "language": "pt"},
    "bg": {"name": "Bulgaria", "language": "bg"},
    "ca": {"name": "Canada", "language": "en"},
    "cn": {"name": "China", "language": "zh"},
    "co": {"name": "Columbia", "language": "es"},
    "cu": {"name": "Cuba", "language": "es"},
    "cz": {"name": "Czech Republic", "language": "cs"},
    "eg": {"name": "Egypt", "language": "ar"},
    "fr": {"name": "France", "language": "fr"},
    "de": {"name": "Germany", "language": "de"},
    "gr": {"name": "Greece", "language": "el"},
    "hk": {"name": "Hong Kong", "language": "zh"},
    "hu": {"name": "Hungary", "language": "hu"},
    "in": {"name": "India", "language": "hi"},
    "id": {"name": "Indonesia", "language": "id"},
    "ie": {"name": "Ireland", "language": "en"},
    "il": {"name": "Israel", "language": "he"},
    "it": {"name": "Italy", "language": "it"},
    "jp": {"name": "Japan", "language": "ja"},
    "lv": {"name": "Latvia", "language": "lv"},
    "lt": {"name": "Lithuania", "language": "lt"},
    "my": {"name": "Malaysia", "language": "ms"},
    "mx": {"name": "Mexico", "language": "es"},
    "ma": {
        "name": "Morocco",
        "language": "fr",
    },  # 'fr'most biz/gov/media, ar used more by population
    "nl": {"name": "Netherlands", "language": "nl"},
    "nz": {"name": "New Zealand", "language": "en"},
    "ng": {"name": "Nigeria", "language": "en"},
    "no": {"name": "Norway", "language": "no"},
    "ph": {"name": "Philippines", "language": "en"},  # 'en' (none for filipino)
    "pl": {"name": "Poland", "language": "pl"},
    "pt": {"name": "Portugal", "language": "pt"},
    "ro": {"name": "Romania", "language": "ro"},
    "ru": {"name": "Russia", "language": "ru"},
    "sa": {"name": "Saudi Arabia", "language": "ar"},
    "rs": {"name": "Serbia", "language": "sr"},
    "sg": {
        "name": "Singapore",
        "language": "en",
    },  # 'en' (malay, ms, is official but en is used for biz/gov/edu)
    "sk": {"name": "Slovakia", "language": "sk"},
    "si": {"name": "Slovenia", "language": "sl"},
    "za": {"name": "South Africa", "language": "en"},
    "kr": {"name": "South Korea", "language": "ko"},
    "se": {"name": "Sweden", "language": "se"},
    "ch": {
        "name": "Switzerland",
        "language": "de",
    },  # 'de' @74%, other official: fr @ 21, it @ 4, and romansh @ 1)
    "tw": {"name": "Taiwan", "language": "zh"},
    "th": {"name": "Thailand", "language": "th"},
    "tr": {"name": "Turkey", "language": "tr"},
    "ae": {"name": "UAE", "language": "en"},
    "ua": {"name": "Ukraine", "language": "uk"},
    "gb": {"name": "United Kingdom", "language": "en"},
    "us": {"name": "United States", "language": "en"},
    "ve": {"name": "Venezuela", "language": "es"},
}

country_codes = {
    "zh": {"name": "China", "language": "zh"},
    "es": {"name": "Spain", "language": "es"},
    "is": {"name": "Israel", "language": "he"},  # 'he' + 'en'     < ICELAND >
    "pk": {"name": "Pakistan", "language": "ud"},
    "ch": {
        "name": "Switzerland",
        "language": "de",
    },  # 'de' @74%, other official: fr @ 21, it @ 4, and romansh @ 1)
    # ONLY THE 2 LETTER CODE IS IN FOR THESE
    "bo": {"Bolivia"},
    "by": {"Belarus"},
    "cl": {"Chile"},
    "ci": {"Cote d'Ivoire"},
    "cr": {"Costa Rica"},
    "ec": {"Ecuador"},
    "fi": {"Finland"},
    "gt": {"Guatamala"},
    "hn": {"honduras"},
    "kz": {"Kazakhstan"},
    "lu": {"Luxembourg"},
    "pa": {"Panama"},
    "pe": {"Peru"},
    "ug": {"Uganda"},
    "uy": {"Uruguay"},
}

NOT_ENTERED_AT_ALL = {
    "ad": "Andorra",
    "af": "Afghanistan",
    "al": "Albania",
    "am": "Armenia",
    "ao": "Angola",
    "as": "American Samoa",
    "az": "Azerbaijan",
    "ba": "Bosnia and Herzegovina",
    "bd": "Bangladesh",
    "bf": "Burkina Faso",
    "bh": "Bahrain",
    "bi": "Burundi",
    "bj": "Benin",
    "bt": "Bhutan",
    "bw": "Botswana",
    "bz": "Belize",
    "cd": "Congo, Democratic Republic of the",
    "cf": "Central African Republic",
    "cg": "Congo",
    "cm": "Cameroon",
    "cy": "Cyprus",
    "cz": "Czech Republic",
    "dj": "Djibout   i",
    "dk": "Denmark",
    "do": "Dominican Republic",
    "dz": "Algeria",
    "ee": "Estonia",
    "er": "Eritrea",
    "et": "Ethiopia",
    "fj": "Fiji",
    "ga": "Gabon",
    "gd": "Grenada",
    "ge": "Georgia",
    "gf": "French Guiana",
    "gh": "Ghana",
    "gi": "Gibraltar",
    "gl": "Greenland",
    "gm": "Gambia",
    "gn": "Guinea",
    "gp": "Guadeloupe",
    "gq": "Equatorial Guinea",
    "gs": "South Georgia",
    "gu": "Guam",
    "gw": "Guinea-Bissau",
    "gy": "Guyana",
    "hr": "Croatia",
    "ht": "Haiti",
    "iq": "Iraq",
    "ir": "Iran",
    "is": "Iceland",
    "jm": "Jamaica",
    "jo": "Jordan",
    "ke": "Kenya",
    "kg": "Kyrgyzstan",
    "kh": "Cambodia",
    "kp": "North Korea",
    "kw": "Kuwait",
    "la": "Laos",
    "lb": "Lebanon",
    "li": "Liechtenstein",
    "lk": "Sri Lanka",
    "lr": "Liberia",
    "ls": "Lesotho",
    "lt": "Lithuania",
    "ly": "Libya",
    "mc": "Monaco",
    "md": "Moldova",
    "me": "Montenegro",
    "mg": "Madagascar",
    "mk": "North Macedonia",
    "ml": "Mali",
    "mm": "Myanmar",
    "mn": "Mongolia",
    "mr": "Mauritania",
    "mt": "Malta",
    "mu": "Mauritius",
    "mv": "Maldives",
    "mw": "Malawi",
    "mz": "Mozambique",
    "na": "Namibia",
    "ne": "Niger",
    "ng": "Nigeria",
    "ni": "Nicaragua",
    "np": "Nepal",
    "om": "Oman",
    "pf": "French Polynesia",
    "pg": "Papua New Guinea",
    "ps": "Palestine",
    "qa": "Qatar",
    "rw": "Rwanda",
    "sd": "Sudan",
    "sl": "Sierra Leone",
    "sn": "Senegal",
    "so": "Somalia",
    "sr": "Suriname",
    "ss": "South Sudan",
    "sv": "El Salvador",
    "sy": "Syria",
    "td": "Chad",
    "tg": "Togo",
    "tj": "Tajikistan",
}