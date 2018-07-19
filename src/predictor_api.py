from flask import Flask
from flask import request
import src.predict.match_result_prediction as match_result_prediction
import src.predict.match_score_prediction as match_score_prediction
import src.train.match_result_train as match_result_train
import src.train.match_score_train as match_score_train
import src.train.player_goals_train as player_goals_train
import src.train.player_score_first_train as player_score_first_train
import src.train.player_score_last_train as player_score_last_train
import src.predict.player_goals_prediction as player_goals_prediction
import src.predict.player_score_first_prediction as player_score_first_prediction
import src.predict.player_score_last_prediction as player_score_last_prediction


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


@app.route('/predict/goals/<type>/country/<country>/<team>',  methods=['POST'])
def predictGoals(type, country, team):
    print(request.data)

    return player_goals_prediction.predict(json.loads(request.data), type, country, team)


@app.route('/predict/first-goal/<type>/country/<country>/<team>',  methods=['POST'])
def predictFirstGoal(type, country, team):
    print(request.data)

    return player_score_first_prediction.predict(json.loads(request.data), type, country, team)


@app.route('/predict/last-goal/<type>/country/<country>/<team>',  methods=['POST'])
def predictLastGoal(type, country, team):
    print(request.data)

    return player_score_last_prediction.predict(json.loads(request.data), type, country, team)

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

# need to also schedule this -- this is for me to get it started.
@app.route('/train/goals', methods=['POST'])
def trainGoals():
    player_goals_train.train()

    return "Done"

# need to also schedule this -- this is for me to get it started.
@app.route('/train/score-first', methods=['POST'])
def trainToScoreFirst():
    player_score_first_train.train()

    return "Done"


# need to also schedule this -- this is for me to get it started.
@app.route('/train/score-last', methods=['POST'])
def trainToScoreLast():
    player_score_last_train.train()

    return "Done"