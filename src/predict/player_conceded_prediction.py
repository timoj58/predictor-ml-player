import dataset.match_dataset as match_dataset
from util.config_utils import get_dir_cfg
import util.train_history_utils as train_history_utils


def predict(player, receipt):

 previous_vocab_date=train_history_utils.get_previous_vocab_date(player)

 predict_process(
    data=data,
    player=player,
    label='conceded',
    label_values=match_dataset.SCORE,
    model_dir="conceded",
    previous_vocab_date=previous_vocab_date,
    receipt=receipt)

