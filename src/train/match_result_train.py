import json
import tensorflow as tf

import model.match_result_model as match_result_model
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
                           "/home/timmytime/IdeaProjects/predictor-ml-model/res/train-matches-"+type+"-"+country+".csv")

         ##take a copy of our file if it doesnt exist.
         if not os.path.isfile("/home/timmytime/IdeaProjects/predictor-ml-model/res/test-matches-"+type+"-"+country+".csv"):
           copyfile("/home/timmytime/IdeaProjects/predictor-ml-model/res/train-matches-"+type+"-"+country+".csv",
                    "/home/timmytime/IdeaProjects/predictor-ml-model/res/test-matches-"+type+"-"+country+".csv")

         match_result_model.create(type, country, True)


