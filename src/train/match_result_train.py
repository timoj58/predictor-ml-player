import json
import tensorflow as tf

import model.match_model as match_model
import dataset.match_dataset as match_dataset
import util.model_utils as model_utils
import util.cache_utils as cache_utils
from shutil import copyfile
from util.file_utils import is_on_file
from util.file_utils import get_aws_file


def train():

    print ('starting...')

    # so get types.
    types = cache_utils.get_types(cache_utils.TYPES_URL)

    for type in types:
     print (type)
     countries = cache_utils.get_countries(cache_utils.COUNTRIES_URL, type)
     for country in countries:
         print (country)
         train_country(type, country)


def train_country(type, country):

   competition_count = cache_utils.get_competitions_per_country(cache_utils.COMPETITIONS_BY_COUNTRY_URL, type, cache_utils)

   data_range = model_utils.data_ranges

   if competition_count > 2:
       data_range = model_utils.data_ranges_4

   for data in data_range:
    model_utils.create_csv(model_utils.EVENT_MODEL_URL + type+"/"+country,
                           model_utils.MODEL_RES_DIR+"train-matches-"+type+"-"+country+".csv", data)

    ##take a copy of our file if it doesnt exist.
    if not is_on_file(model_utils.MODEL_RES_DIR+"test-matches-"+type+"-"+country+".csv"):
        copyfile(model_utils.MODEL_RES_DIR+"train-matches-"+type+"-"+country+".csv",
                 model_utils.MODEL_RES_DIR+"test-matches-"+type+"-"+country+".csv")
    else:
        get_aws_file('',  "test-matches-"+type+"-"+country+".csv")

    match_model.create(type, country, True, 'outcome', match_dataset.OUTCOMES, "match_result", "matches-", False)
