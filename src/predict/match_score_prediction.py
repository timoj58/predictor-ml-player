from predict.match_predict import predict as predict_process
import dataset.match_dataset as match_dataset


def predict(data, type, country, receipt):

    return predict_process(
        data,
        type,
        country,
        'scoreOutcome',
        match_dataset.SCORE_OUTCOMES,
        "match_score",
        True,
        receipt)
