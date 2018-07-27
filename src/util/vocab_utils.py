import requests
from requests.auth import HTTPDigestAuth
import json
import auth_utils as auth_utils
from datetime import date
import config_utils as config_utils

TEAMS_URL = config_utils.get_vocab_cfg()['team_vocab_url']
PLAYERS_URL = config_utils.get_vocab_cfg()['player_vocab_url']

TEAMS_FILE = config_utils.get_vocab_cfg()['team_vocab_file']
PLAYERS_FILE = config_utils.get_vocab_cfg()['player_vocab_file']

def create_vocab(url, filename, type, country):

    response = requests.get(url+"?type="+type+"&country="+country,headers={'application-token': auth_utils.auth()})
    values = response.json()

    size = 0

    with open(filename+"-"+type+"-"+country+ ".txt", 'w') as f:
        for value in values:
            label = value['id']
            if label is not None:
                f.write(label.encode('unicode_escape'))
                f.write('\n')
                size += 1

    return size