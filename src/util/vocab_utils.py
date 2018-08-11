import requests
from requests.auth import HTTPDigestAuth
import json
from util.auth_utils import auth
from util.config_utils import get_vocab_cfg
from util.file_utils import is_on_file
from util.file_utils import put_aws_file_with_path
from util.file_utils import get_aws_file
from util.file_utils import write_filenames_index_from_filename
from util.file_utils import make_dir
import datetime
from datetime import date, timedelta
import logging
from util.config_utils import get_dir_cfg
import os.path
import os

logger = logging.getLogger(__name__)


docker_host = get_dir_cfg()['docker_host']


TEAMS_URL = docker_host+get_vocab_cfg()['team_vocab_url']
PLAYERS_URL = docker_host+get_vocab_cfg()['player_vocab_url']
PLAYERS_BY_COUNTRY_URL = docker_host+get_vocab_cfg()['player_by_country_vocab_url']


local_dir = get_dir_cfg()['local']
TEAMS_FILE = 'team-vocab'
PLAYERS_FILE = 'player-vocab'
PLAYERS_BY_COUNTRY_FILE = 'player-by-country-vocab'


def create_vocab(url, filename, type, country, player_id):

  vocab_path = get_dir_cfg()['vocab_path']

  if url == PLAYERS_URL:
    url = url+"?player-id="+player_id
    vocab_path = vocab_path.replace('<type>', type)
    vocab_path = vocab_path.replace('<key>', player_id)

    previous_filename = local_dir+vocab_path+filename+"-"+str(datetime.date.today() - timedelta(1))+".txt"
    filename =  local_dir+vocab_path+filename+"-"+str(datetime.date.today())+".txt"
  else:
    url = url+"?type="+type+"&country="+country

    vocab_path = vocab_path.replace('<type>', type)
    vocab_path = vocab_path.replace('<key>', country)

    previous_filename =  local_dir+vocab_path+filename+"-"+str(datetime.date.today() - timedelta(1))+".txt"
    filename =  local_dir+vocab_path+filename+"-"+str(datetime.date.today())+".txt"

  logger.info('checking for '+filename)

  if not is_on_file(filename):

    response = requests.get(url,headers={'application-token': auth()})
    values = response.json()


    if is_on_file(previous_filename):
      logger.info('vocab '+previous_filename+' is on file')
      # now load the new file to memory.  and only add in values that arent in the list to the end.
      patch_vocab(filename, previous_filename, values)
    else:
        logger.info('vocab '+previous_filename+' is not on file')
        make_dir(filename)
        with open(filename, 'w') as f:
            for value in values:
                label = value['id']
                if label is not None:
                    f.write(label)
                    f.write('\n')

    # now put file away.
    head, tail = os.path.split(filename)
    put_aws_file_with_path(vocab_path, tail)
    write_filenames_index_from_filename(filename)

  else:
    head, tail = os.path.split(filename)
    logger.info('get from aws '+tail)
    #need to load the file from aws potentially
    get_aws_file(vocab_path, tail)

  return filename


def patch_vocab(filename, previous_filename, values):
    make_dir(filename)
    with open(previous_filename, 'r') as f:
        previous = f.read().splitlines()
    # now write all these to new file.  stupid tensorflow order issue
    with open(filename, 'w') as f:
        logger.info('adding old records to new file')
        for value in previous:
            f.write(value.strip('\n'))
            f.write('\n')
            #now append any new ones
    with open(filename, 'a') as f:
        logger.info('now trying to append any new entries')
        for value in values:
            label = value['id']
            if label is not None:
                if label not in previous:
                    logger.info('adding a new entry to file '+label)
                    f.write(label)
                    f.write('\n')

    logger.info('finished fecking about with vocab')



