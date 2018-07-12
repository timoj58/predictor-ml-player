import requests
from requests.auth import HTTPDigestAuth
import json
import auth_utils as auth_utils

TEAMS_URL = "http://localhost:8090/api/prediction/teams"
PLAYERS_URL = "http://localhost:8090/api/prediction/players"

TEAMS_FILE = '/home/timmytime/IdeaProjects/predictor-ml-model/res/team-vocab.txt'
PLAYERS_FILE = '/home/timmytime/IdeaProjects/predictor-ml-model/res/player-vocab.txt'

def create_vocab(url, filename):

    response = requests.get(url,headers={'application-token': auth_utils.auth()})
    values = response.json()

    size = 0

    with open(filename, 'w') as f:
        for value in values:
            label = value['id']
            if label is not None:
                f.write(label.encode('unicode_escape'))
                f.write('\n')
                size += 1

    return size