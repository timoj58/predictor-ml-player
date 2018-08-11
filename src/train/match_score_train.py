import model.match_model as match_model
import dataset.match_dataset as match_dataset
import util.model_utils as model_utils
import util.cache_utils as cache_utils
import util.receipt_utils as receipt_utils
from shutil import copyfile
from util.file_utils import is_on_file
from util.file_utils import get_aws_file
from util.file_utils import put_aws_file_with_path
from util.config_utils import get_analysis_cfg
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
            train_country(type, country, receipt)

    receipt_utils.put_receipt(receipt_utils.TRAIN_RECEIPT_URL, receipt, None)


def train_country(type, country, receipt):

    train_path = get_dir_cfg()['train_path']
    train_path = train_path.replace('<type>', type)
    train_path = train_path.replace('<key>', country)

    competition_count = cache_utils.get_competitions_per_country(cache_utils.COMPETITIONS_BY_COUNTRY_URL, type, cache_utils)

    if get_analysis_cfg()['historic']:
     data_range = model_utils.data_ranges

     if competition_count > 2:
        data_range = model_utils.data_ranges_4
    else:
        data_range = model_utils.real_time_range

    for data in data_range:

     train_filename = "train-scores"+data.replace('/','-')+".csv"
     test_filename = "test-scores"+data.replace('/','-')+".csv"


     has_data = model_utils.create_csv(model_utils.EVENT_MODEL_URL + type+"/"+country,
                                       local_dir+train_path+train_filename,data, train_path)

     if has_data:
      ##take a copy of our file if it doesnt exist.
      if not is_on_file(local_dir+train_path+test_filename):
        copyfile(local_dir+train_path+train_filename,
                 local_dir+train_path+test_filename)
        put_aws_file_with_path(train_path,test_filename)
      else:
        get_aws_file(train_path,  test_filename)

      match_model.create(type, country, True,'scoreOutcome', match_dataset.SCORE_OUTCOMES,
                         "match_score", local_dir+train_path+train_filename, local_dir+train_path+test_filename, True)
     else:
         logger.info ('no data to train')

    if receipt is not None:
     receipt_utils.put_receipt(receipt_utils.TRAIN_RECEIPT_URL, receipt, None)
