from predict.match_predict import predict as predict_process
import dataset.match_dataset as match_dataset
import util.train_history_utils as train_history_utils


def predict(data, type, country, receipt):

    previous_vocab_date=train_history_utils.get_previous_vocab_date(country)

    return predict_process(
        data=data,
        type=type,
        country=country,
        label='scoreOutcome',
        label_values=match_dataset.SCORE_OUTCOMES,
        model_dir="match_score",
        outcome=True,
        previous_vocab_date=previous_vocab_date,
        receipt=receipt)
