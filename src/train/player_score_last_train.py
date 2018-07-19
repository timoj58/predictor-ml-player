import json
import tensorflow as tf

import model.player_model as player_model
import dataset.player_dataset as player_dataset
import util.model_utils as model_utils
import util.cache_utils as cache_utils
import util.vocab_utils as vocab_utils
from shutil import copyfile
import os.path


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
                model_utils.create_csv(model_utils.PLAYER_MODEL_URL + team,
                                   model_utils.MODEL_RES_DIR+"train-player-last-goal-"+type+"-"+country+"-"+team+".csv")

                ##take a copy of our file if it doesnt exist.
                if not os.path.isfile(model_utils.MODEL_RES_DIR+"test-player-last-goal-"+type+"-"+country+"-"+team+".csv"):
                 copyfile(model_utils.MODEL_RES_DIR+"train-player-last-goal-"+type+"-"+country+"-"+team+".csv",
                          model_utils.MODEL_RES_DIR+"test-player-last-goal-"+type+"-"+country+"-"+team+".csv")

                player_model.create(type, country,team, True, 'lastGoal', player_dataset.FIRST_LAST_OUTCOMES, "player_last_goal", "player-last-goal-", False)


