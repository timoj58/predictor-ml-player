from predict.match_predict import predict as predict_process
import dataset.match_dataset as match_dataset
from util.config_utils import get_dir_cfg
import util.train_history_utils as train_history_utils


def predict(player, receipt):

 previous_vocab_date=train_history_utils.get_previous_vocab_date(player)

 predict_process(
    data=data,
    player=player,
    label='assists',
    label_values=match_dataset.NUMERICS,
    model_dir="assists",
    previous_vocab_date=previous_vocab_date,
    receipt=receipt)

