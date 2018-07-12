import requests
from requests.auth import HTTPDigestAuth
import csv
import auth_utils as auth_utils

PLAYER_MODEL_URL = "http://localhost:8090/api/prediction/ml-data/players/"
EVENT_MODEL_URL = "http://localhost:8090/api/prediction/ml-data/competition/"

def create_csv(url, filename):
    print ('getting csv data...')
    data = requests.get(url+'/02-01-2018/12-07-2018', headers={'application-token': auth_utils.auth()})

    with open(filename, 'w') as f:
     writer = csv.writer(f)
     reader = csv.reader(data.text.splitlines())

     for row in reader:
      writer.writerow(row)

    print ('created csv')
