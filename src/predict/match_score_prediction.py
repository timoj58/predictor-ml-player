import match_predict as match_predict
import dataset.match_dataset as match_dataset


def predict(data, type, country):

    return match_predict.predict(
        data,
        type,
        country,
        'scoreOutcome',
        match_dataset.SCORE_OUTCOMES,
        "match_score",
        "scores-",
        True)
