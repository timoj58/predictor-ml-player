import requests
from requests.auth import HTTPDigestAuth
import json
import auth_utils as auth_utils

TYPES_URL = "http://localhost:8090/api/prediction/cache/types"
COUNTRIES_URL = "http://localhost:8090/api/prediction/cache/countries"


def get_types(url):

    response = requests.get(url, headers={'application-token': auth_utils.auth()})
    values = response.json()

    types = []

    for value in values:
        types.append(value['type'])

    return types

def get_countries(url, type):

    response = requests.get(url+"?type="+type, headers={'application-token': auth_utils.auth()})
    values = response.json()

    countries = []

    for value in values:
     countries.append(value['country'])

    return countries

def get_teams(url, type, country):

    response = requests.get(url+"?type="+type+"&country="+country, headers={'application-token': auth_utils.auth()})
    values = response.json()

    teams = []

    for value in values:
        label = value['id']
        if label is not None:
            teams.append(label.encode('unicode_escape'))

    return teams