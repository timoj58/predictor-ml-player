from predict.match_predict import predict as predict_process
import dataset.match_dataset as match_dataset


def predict(data, type, country, receipt):

    return predict_process(
        data=data,
        type=type,
        country=country,
        label='scoreOutcome',
        label_values=match_dataset.SCORE_OUTCOMES,
        model_dir="match_score",
        outcome=True,
        receipt=receipt)
