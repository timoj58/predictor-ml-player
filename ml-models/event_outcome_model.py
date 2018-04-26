import tensorflow as tf
import requests
from requests.auth import HTTPDigestAuth
import json

TEAMS_URL = "http://localhost:8090/api/prediction/teams"
PLAYERS_URL = "http://localhost:8090/api/prediction/players"


def create_vocab(url, filename):
 
  response = requests.get(url)
  values = response.json()
  
  with open(filename, 'w') as f:
   for value in values:
     label = value['label']
     if label is not None:
       f.write(label.encode('unicode_escape')) 
       f.write('\n')

def main(argv):

 create_vocab(TEAMS_URL, 'team-vocab.txt');
 create_vocab(PLAYERS_URL, 'player-vocab.txt');


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)











