from predict.match_predict import predict as predict_process
import dataset.match_dataset as match_dataset
from util.config_utils import get_dir_cfg
import util.train_history_utils as train_history_utils


local_dir = get_dir_cfg()['local']
history_file = get_dir_cfg()['country_results_train_history_file']

def predict(data, type, country, receipt):

 previous_vocab_date=train_history_utils.get_previous_vocab_date(history_file, country)

 predict_process(
    data=data,
    type=type,
    country=country,
    label='outcome',
    label_values=match_dataset.OUTCOMES,
    model_dir="match_result",
    outcome=False,
    previous_vocab_date=previous_vocab_date,
    receipt=receipt)

