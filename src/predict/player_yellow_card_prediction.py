from predict.player_predict import predict as predict_process
import dataset.match_dataset as match_dataset
from util.config_utils import get_dir_cfg
import util.train_history_utils as train_history_utils


def predict(data, player, receipt):


    predict_process(
        data=data,
        player=player,
        label='yellow',
        label_values=match_dataset.CARDS,
        model_dir="yellow",
        receipt=receipt)

