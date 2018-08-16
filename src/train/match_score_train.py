import util.model_utils as model_utils
import util.cache_utils as cache_utils
import util.receipt_utils as receipt_utils
import util.training_utils as training_utils
import util.train_history_utils as train_history_utils
from util.config_utils import get_dir_cfg
from util.config_utils import get_learning_cfg
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

    learning_cfg = get_learning_cfg(country)

    train_path = get_dir_cfg()['train_path']
    train_path = train_path.replace('<type>', type)
    train_path = train_path.replace('<key>', country)

    history = train_history_utils.init_history('in progress',learning_cfg)

    competition_count = cache_utils.get_competitions_per_country(cache_utils.COMPETITIONS_BY_COUNTRY_URL, type, cache_utils)

    if learning_cfg['historic']:
     data_range = model_utils.create_range(int(learning_cfg['months_per_cycle']), learning_cfg)

     if competition_count > 2:
        data_range = model_utils.create_range(int(learning_cfg['months_per_cycle']/2), learning_cfg)

    else:
     data_range = model_utils.real_time_range


    training_utils.train_match(
                         type=type,
                         country=country,
                         data_range=data_range,
                         filename_prefix="scores",
                         label='scoreOutcome',
                         model_dir="match_score",
                         train_path=train_path,
                         receipt=receipt,
                         history=history)

