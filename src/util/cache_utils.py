import requests
from requests.auth import HTTPDigestAuth
import json
from util.auth_utils import auth
from util.config_utils import get_analysis_cfg
from util.config_utils import get_dir_cfg

docker_host = get_dir_cfg()['docker_host']

TYPES_URL = docker_host+get_analysis_cfg()['types_url']
COUNTRIES_URL = docker_host+get_analysis_cfg()['countries_url']
COMPETITIONS_BY_COUNTRY_URL = docker_host+get_analysis_cfg()['comps_by_country_url']


def get_types(url):

    response = requests.get(url, headers={'application-token': auth()})
    values = response.json()

    types = []

    for value in values:
        types.append(value['type'])

    return types

def get_countries(url, type):

    response = requests.get(url+"?type="+type, headers={'application-token': auth()})
    values = response.json()

    countries = []

    for value in values:
     countries.append(value['country'])

    return countries

def get_teams(url, type, country):

    response = requests.get(url+"?type="+type+"&country="+country, headers={'application-token': auth()})
    values = response.json()

    teams = []

    for value in values:
        label = value['id']
        if label is not None:
            teams.append(label.encode('unicode_escape'))

    return teams


def get_competitions_per_country(url, type, country):
    response = requests.get(url+"?type="+type+"&country="+country, headers={'application-token': auth()})
    return response.json()['count']

