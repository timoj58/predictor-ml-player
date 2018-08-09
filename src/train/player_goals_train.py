import json
import tensorflow as tf

import model.player_model as player_model
import dataset.player_dataset as player_dataset
import util.model_utils as model_utils
import util.cache_utils as cache_utils
import util.vocab_utils as vocab_utils
from shutil import copyfile
from util.file_utils import is_on_file
from util.file_utils import get_aws_file
from util.file_utils import put_aws_file
from util.config_utils import get_analysis_cfg
from util.config_utils import get_dir_cfg
import logging

logger = logging.getLogger(__name__)


local_dir = get_dir_cfg()['local']


def train_player(type, country, player, receipt):

    process(type, country, player)


def train(receipt):

    logger.info ('starting...')

    # so get types.
    types = cache_utils.get_types(cache_utils.TYPES_URL)

    for type in types:
        logger.info (type)
        countries = cache_utils.get_countries(cache_utils.COUNTRIES_URL, type)
        for country in countries:
          logger.info (country)
          teams = cache_utils.get_teams(vocab_utils.TEAMS_URL, type, country)
          for team in teams:
             logger.info(team)
             players = cache_utils.get_players(cache_utils.PLAYERS_BY_TEAM_URL, team)
             for player in players:
              logger.info(player)
              process(type, country, player)


def process(type, country, player):

    if get_analysis_cfg()['historic']:
        range = model_utils.player_historic_range
    else:
       range = model_utils.real_time_range[0]

    has_data = model_utils.create_csv(model_utils.PLAYER_MODEL_URL +player,
                                      local_dir+"train-player-goals-"+type+"-"+country+"-"+player+".csv", range)

    if has_data:
     ##take a copy of our file if it doesnt exist.
     if not is_on_file(local_dir+"test-player-goals-"+type+"-"+country+"-"+player+".csv"):
        copyfile(local_dir+"train-player-goals-"+type+"-"+country+"-"+player+".csv",
                 local_dir+"test-player-goals-"+type+"-"+country+"-"+player+".csv")
        put_aws_file(local_dir+"test-player-goals-"+type+"-"+country+".csv")
     else:
        get_aws_file('',  "test-player-goals-"+type+"-"+country+"-"+player+".csv")


     player_model.create(type, country, player, True, 'goals', player_dataset.GOALS_OUTCOMES, "player_goals", "player-goals-", False)
    else:
      logger.info ('no data to train')
