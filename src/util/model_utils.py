import requests
from requests.auth import HTTPDigestAuth
import csv
import auth_utils as auth_utils
import config_utils as config_utils

PLAYER_MODEL_URL = config_utils.get_analysis_cfg()['player_model_url']
EVENT_MODEL_URL = config_utils.get_analysis_cfg()['team_model_url']


MODEL_RES_DIR = config_utils.get_dir_cfg()['models']
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
