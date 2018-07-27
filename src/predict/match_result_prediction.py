import match_predict as match_predict
import dataset.match_dataset as match_dataset


def predict(data, type, country):

    return match_predict.predict(
        data,
        type,
        country,
        'outcome',
        match_dataset.OUTCOMES,
        "match_result",
        "matches-",
        False)

