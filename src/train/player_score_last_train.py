import util.model_utils as model_utils
import util.cache_utils as cache_utils
import util.vocab_utils as vocab_utils
import util.receipt_utils as receipt_utils
import util.training_utils as training_utils
import util.train_history_utils as train_history_utils
from util.config_utils import get_learning_cfg
from util.config_utils import get_dir_cfg
import logging

logger = logging.getLogger(__name__)


local_dir = get_dir_cfg()['local']
history_file = get_dir_cfg()['players_last_goal_train_history_file']


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

    learning_cfg = get_learning_cfg('player')

    train_path = get_dir_cfg()['train_path']
    train_path = train_path.replace('<type>', type)
    train_path = train_path.replace('<key>', country)+player+"/"

    previous_vocab_date=train_history_utils.get_previous_vocab_date(history_file, country)
    history = train_history_utils.init_history('in progress',learning_cfg)

    if learning_cfg['historic']:
        range = model_utils.player_historic_range
    else:
        range = model_utils.real_time_range(
            start_day=train_history_utils.get_history(filename=history_file, key='end_day'),
            start_month=train_history_utils.get_history(filename=history_file, key='end_month'),
            start_year=train_history_utils.get_history(filename=history_file, key='end_year'))


    training_utils.train_player(
        type=type,
        country=country,
        player=player,
        range=range,
        filename_prefix="player-last-goal",
        label='lastGoal',
        model_dir="player_last_goal",
        train_path=train_path,
        history=history,
        previous_vocab_date=previous_vocab_date)
