from predict.match_predict import predict as predict_process
import dataset.match_dataset as match_dataset


def predict(data, type, country, receipt):

    return predict_process(
        data=data,
        type=type,
        country=country,
        label='goals',
        label_values=match_dataset.GOALS,
        model_dir="match_goals",
        outcome=False,
        previous_vocab_date="XX-XX-XXXX",
        receipt=receipt)
