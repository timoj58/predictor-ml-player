from flask import Flask
from flask import request
import src.predict.match_result_prediction as match_result_prediction
import src.train.match_result_train as match_result_train
import json

app = Flask(__name__)

## needs exception handling etc. for now its ok.

@app.route('/predict/result/<type>/country/<country>',  methods=['POST'])
def predictResult(type, country):
    print(request.data)

    return match_result_prediction.predict(json.loads(request.data), type, country)

# need to also schedule this -- this is for me to get it started.
@app.route('/train', methods=['POST'])
def train():
    match_result_train.train()

