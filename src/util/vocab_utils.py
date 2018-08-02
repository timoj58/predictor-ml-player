import requests
from requests.auth import HTTPDigestAuth
import json
from util.auth_utils import auth
from datetime import date
from util.config_utils import get_vocab_cfg
from util.file_utils import is_on_file
from util.file_utils import put_aws_file
from util.file_utils import get_aws_file
from util.file_utils import write_filenames_index_from_filename
import datetime

TEAMS_URL = get_vocab_cfg()['team_vocab_url']
PLAYERS_URL = get_vocab_cfg()['player_vocab_url']
PLAYERS_BY_COUNTRY_URL = get_vocab_cfg()['player_by_country_vocab_url']


TEAMS_FILE = get_vocab_cfg()['team_vocab_file']
PLAYERS_FILE = get_vocab_cfg()['player_vocab_file']
PLAYERS_BY_COUNTRY_FILE = get_vocab_cfg()['player_by_country_vocab_file']


def create_vocab(url, filename, type, country, player_id):
  if url == PLAYERS_URL:
    url = url+"?player-id="+player_id
    filename =  filename+"-"+type+"-"+player_id+"-"+str(datetime.date.today())+ ".txt"
  else:
    url = url+"?type="+type+"&country="+country
    filename =  filename+"-"+type+"-"+country+"-"+str(datetime.date.today())+ ".txt"

  if not is_on_file(filename):

    response = requests.get(url,headers={'application-token': auth()})
    values = response.json()


    with open(filename, 'w') as f:
        for value in values:
            label = value['id']
           # print(label)
            if label is not None:
                f.write(label)
                f.write('\n')

    put_aws_file('', filename)
    write_filenames_index_from_filename(filename)

  else:
    #need to load the file from aws potentially
    get_aws_file('', filename, '')

  return filename

