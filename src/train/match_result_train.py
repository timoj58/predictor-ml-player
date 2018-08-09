import json
import tensorflow as tf

import model.match_model as match_model
import dataset.match_dataset as match_dataset
import util.model_utils as model_utils
import util.cache_utils as cache_utils
import util.receipt_utils as receipt_utils
from shutil import copyfile
from util.file_utils import is_on_file
from util.file_utils import get_aws_file
from util.file_utils import put_aws_file
from util.config_utils import get_analysis_cfg
import datetime
from util.config_utils import get_dir_cfg
import logging

logger = logging.getLogger(__name__)


local_dir = get_dir_cfg()['local']


def train(receipt):

    logger.info ('starting...')

    # so get types.
    types = cache_utils.get_types(cache_utils.TYPES_URL)

    for type in types:
     logger.info (type)
     countries = cache_utils.get_countries(cache_utils.COUNTRIES_URL, type)
     for country in countries:
         logger.info (country)
         train_country(type, country, None)

     receipt_utils.put_receipt(receipt_utils.TRAIN_RECEIPT_URL, receipt, None)

def train_country(type, country, receipt):

   competition_count = cache_utils.get_competitions_per_country(cache_utils.COMPETITIONS_BY_COUNTRY_URL, type, country)

   if get_analysis_cfg()['historic']:
    data_range = model_utils.data_ranges

    if competition_count > 2:
       data_range = model_utils.data_ranges_4
   else:
       data_range = model_utils.real_time_range

   for data in data_range:
    has_data = model_utils.create_csv(model_utils.EVENT_MODEL_URL + type+"/"+country,
                                      local_dir+"train-matches-"+type+"-"+country+".csv", data)

    if has_data:
     ##take a copy of our file if it doesnt exist.
     if not is_on_file(local_dir+"test-matches-"+type+"-"+country+".csv"):
         copyfile(local_dir+"train-matches-"+type+"-"+country+".csv",
                  local_dir+"test-matches-"+type+"-"+country+".csv")
         put_aws_file(local_dir+"test-matches-"+type+"-"+country+".csv")
     else:
        get_aws_file('',  "test-matches-"+type+"-"+country+".csv")

     match_model.create(type, country, True, 'outcome', match_dataset.OUTCOMES, "match_result", "matches-", False)
    else:
        logger.info ('no data to train')

    if receipt is not None:
        receipt_utils.put_receipt(receipt_utils.TRAIN_RECEIPT_URL, receipt, None)

