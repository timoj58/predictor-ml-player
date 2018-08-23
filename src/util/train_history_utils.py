import json
import os.path
import logging
import datetime

from util.config_utils import get_dir_cfg

logger = logging.getLogger(__name__)
local_dir = get_dir_cfg()['local']

def write_history(filename, history):
    with open(local_dir+filename, 'w') as outfile:
        json.dump(history, outfile)

def read_history(filename):
    if os.path.isfile(local_dir+filename):
        with open(local_dir+filename) as f:
            return json.load(f)
    else:
        return {}


def get_history(filename, key):
    history = read_history(filename)
    if key in history:
        return history[key]

    return {}


def add_history(filename, key, history):
    all_history = read_history(filename)
    all_history[key] = history
    write_history(filename, all_history)


def create_history(status, start_day, start_month, start_year, end_day, end_month, end_year, vocab_date):
    record = {}
    record['status'] = status
    record['start_day'] = start_day
    record['start_month'] = start_month
    record['start_year'] = start_year
    record['end_day'] = end_day
    record['end_month'] = end_month
    record['end_year'] = end_year
    record['vocab_date'] = vocab_date

    return record


def init_history(status, learning_cfg):
    return create_history(
              status,
              learning_cfg['start_day'],
              learning_cfg['start_month'],
              learning_cfg['start_year'],
              learning_cfg['end_day'],
              learning_cfg['end_month'],
              learning_cfg['end_year'],
              str(datetime.date.today()))


def get_previous_vocab_date(file, key):

   previous_history = get_history(
        filename=file,
        key=key)

   previous_vocab_date="XX-XX-XXXX" #default when cant find

   if 'vocab_date' in previous_history:
    previous_vocab_date=previous_history['vocab_date']

   return previous_vocab_date