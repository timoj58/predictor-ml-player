import json
import tensorflow as tf

import model.player_model as player_model
import dataset.player_dataset as player_dataset
import util.model_utils as model_utils
import util.cache_utils as cache_utils
import util.vocab_utils as vocab_utils
from shutil import copyfile
import os.path


def train_player(type, country, player):

    process(type, country, player, model_utils.PLAYER_MODEL_URL)


def train():

    print ('starting...')

    # so get types.
    types = cache_utils.get_types(cache_utils.TYPES_URL)

    for type in types:
        print (type)
        countries = cache_utils.get_countries(cache_utils.COUNTRIES_URL, type)
        for country in countries:
          print (country)
          teams = cache_utils.get_teams(vocab_utils.TEAMS_URL, type, country)
          for team in teams:
             print(team)
             players = cache_utils.get_players(cache_utils.PLAYERS_BY_TEAM_URL, team)
             for player in players:
              print(player)
              process(type, country, player, model_utils.PLAYER_MODEL_URL)


def process(type, country, player, url):

    model_utils.create_csv(url +player,
                           model_utils.MODEL_RES_DIR+"train-player-goals-"+type+"-"+country+"-"+player+".csv")

    ##take a copy of our file if it doesnt exist.
    if not os.path.isfile(model_utils.MODEL_RES_DIR+"test-player-goals-"+type+"-"+country+"-"+player+".csv"):
        copyfile(model_utils.MODEL_RES_DIR+"train-player-goals-"+type+"-"+country+"-"+player+".csv",
                 model_utils.MODEL_RES_DIR+"test-player-goals-"+type+"-"+country+"-"+player+".csv")

    player_model.create(type, country, player, True, 'goals', player_dataset.GOALS_OUTCOMES, "player_goals", "player-goals-", None)

