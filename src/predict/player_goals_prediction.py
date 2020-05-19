from predict.player_predict import predict as predict_process
import dataset.match_dataset as match_dataset
import util.train_history_utils as train_history_utils

def predict(data, player, receipt):

    previous_vocab_date=train_history_utils.get_previous_vocab_date(player)

    predict_process(
        data=data,
        player=player,
        label='goals',
        label_values=match_dataset.SCORE,
        model_dir="goals",
        previous_vocab_date=previous_vocab_date,
        receipt=receipt)
