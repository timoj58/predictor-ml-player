import requests
from requests.auth import HTTPDigestAuth
import csv
import auth_utils as auth_utils

PLAYER_BY_TEAM_MODEL_URL = "http://localhost:8090/api/prediction/ml-data/players/team/"
PLAYER_MODEL_URL = "http://localhost:8090/api/prediction/ml-data/players/player/"
EVENT_MODEL_URL = "http://localhost:8090/api/prediction/ml-data/competition/"


MODEL_RES_DIR = "/home/timmytime/IdeaProjects/predictor-ml-model/res/"
MODELS_DIR =MODEL_RES_DIR+"models/"

def create_csv(url, filename):
    print ('getting csv data...')
    data = requests.get(url+'/01-08-2013/17-07-2018', headers={'application-token': auth_utils.auth()})

    with open(filename, 'w') as f:
     writer = csv.writer(f)
     reader = csv.reader(data.text.splitlines())

     for row in reader:
      writer.writerow(row)

    print ('created csv')
