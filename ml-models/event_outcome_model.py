import tensorflow as tf

import requests
from requests.auth import HTTPDigestAuth
import json

TEAMS_URL = "http://localhost:8090/api/prediction/teams"
PLAYERS_URL = "http://localhost:8090/api/prediction/players"

teamsResponse = requests.get(TEAMS_URL)
playersResponse = requests.get(PLAYERS_URL)

teams = teamsResponse.json()
players = playersResponse.json()


 


with open('team-vocab.txt', 'w') as f:
 for team in teams:
     label = team['label']
     if label is not None:
       f.write(label.decode('unicode_escape'))

with open('player-vocab.txt', 'w') as f:
  for player in players:
     label = player['label']
     if label is not None:     
      f.write(label.decode('unicode_escape'))








