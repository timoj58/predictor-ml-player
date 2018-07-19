from flask import Flask
from flask import request
import src.predict.match_result_prediction as match_result_prediction
import src.predict.match_score_prediction as match_score_prediction
import src.train.match_result_train as match_result_train
import src.train.match_score_train as match_score_train
import json

app = Flask(__name__)

## needs exception handling etc. for now its ok.

@app.route('/predict/result/<type>/country/<country>',  methods=['POST'])
def predictResult(type, country):
    print(request.data)

    return match_result_prediction.predict(json.loads(request.data), type, country)

@app.route('/predict/score/<type>/country/<country>',  methods=['POST'])
def predictScore(type, country):
    print(request.data)

    return match_score_prediction.predict(json.loads(request.data), type, country)


# need to also schedule this -- this is for me to get it started.
@app.route('/train/results', methods=['POST'])
def trainResults():
    match_result_train.train()

    return "Done"

# need to also schedule this -- this is for me to get it started.
@app.route('/train/scores', methods=['POST'])
def trainScores():
    match_score_train.train()

    return "Done"