import json
import tensorflow as tf

import model.match_model as match_model
import dataset.match_dataset as match_dataset
import util.model_utils as model_utils
import util.cache_utils as cache_utils
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
            model_utils.create_csv(model_utils.EVENT_MODEL_URL + type+"/"+country,
                                   model_utils.MODEL_RES_DIR+"train-scores-"+type+"-"+country+".csv")

            ##take a copy of our file if it doesnt exist.
            if not os.path.isfile(model_utils.MODEL_RES_DIR+"test-scores-"+type+"-"+country+".csv"):
                copyfile(model_utils.MODEL_RES_DIR+"train-scores-"+type+"-"+country+".csv",
                         model_utils.MODEL_RES_DIR+"test-scores-"+type+"-"+country+".csv")

            match_model.create(type, country, True,'scoreOutcome', match_dataset.SCORE_OUTCOMES, "match_score")


