from predict.match_predict import predict as predict_process
import dataset.match_dataset as match_dataset


def predict(data, type, country, receipt):

 predict_process(
    data=data,
    type=type,
    country=country,
    label='outcome',
    label_values=match_dataset.OUTCOMES,
    model_dir="match_result",
    outcome=False,
    receipt=receipt)

