import model.player_model as player_model
import dataset.player_dataset as player_dataset
import util.model_utils as model_utils
import util.cache_utils as cache_utils
import util.vocab_utils as vocab_utils
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


def train_player(type, country, player, receipt):
    process(type, country, player)
    receipt_utils.put_receipt(receipt_utils.TRAIN_RECEIPT_URL, receipt, None)


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

    receipt_utils.put_receipt(receipt_utils.TRAIN_RECEIPT_URL, receipt, None)


def process(type, country, player):

    train_path = get_dir_cfg()['train_path']
    train_path = train_path.replace('<type>', type)
    train_path = train_path.replace('<key>', country)+player+"/"

    if get_analysis_cfg()['historic']:
        range = model_utils.player_historic_range
    else:
        range = model_utils.real_time_range[0]

    train_filename = "train-player-last-goal"+range.replace('/','-')+".csv"
    test_filename = "test-player-last-goal.csv"

    train_file_path = local_dir+train_path+train_filename
    test_file_path = local_dir+train_path+test_filename


    has_data = model_utils.create_csv(model_utils.PLAYER_MODEL_URL + player,
                                      train_file_path, range)

    if has_data:
     ##take a copy of our file if it doesnt exist.
     if not is_on_file(test_file_path):
        copyfile(train_file_path,test_file_path)
        put_aws_file_with_path(train_path, test_filename)
     else:
        get_aws_file(train_path, test_filename)

     player_model.create(type, country,player, True, 'lastGoal', player_dataset.FIRST_LAST_OUTCOMES, "player_last_goal",
                         train_path+train_filename, train_path+test_filename, True)
    else:
        logger.info ('no data to train')