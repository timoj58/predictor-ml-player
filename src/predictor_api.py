from flask import Flask
from flask import request
import predict.match_result_prediction as match_result_prediction
import predict.match_score_prediction as match_score_prediction
import train.match_result_train as match_result_train
import train.match_score_train as match_score_train
import train.player_goals_train as player_goals_train
import train.player_score_first_train as player_score_first_train
import train.player_score_last_train as player_score_last_train
import predict.player_goals_prediction as player_goals_prediction
import predict.player_score_first_prediction as player_score_first_prediction
import predict.player_score_last_prediction as player_score_last_prediction


import json

app = Flask(__name__)

## needs exception handling etc. for now its ok.

@app.route('/predict/result/<type>/country/<country>',  methods=['POST'])
def predict_result(type, country):
    print(request.data)

    return match_result_prediction.predict(json.loads(request.data), type, country)

@app.route('/predict/score/<type>/country/<country>',  methods=['POST'])
def predict_score(type, country):
    print(request.data)

    return match_score_prediction.predict(json.loads(request.data), type, country)


@app.route('/predict/goals/<type>/country/<country>/<player>',  methods=['POST'])
def predict_goals_player(type, country, player):
    print(request.data)

    return player_goals_prediction.predict(json.loads(request.data), type, country, player)


@app.route('/predict/first-goal/<type>/country/<country>/<player>',  methods=['POST'])
def predict_first_goal(type, country, player):
    print(request.data)

    return player_score_first_prediction.predict(json.loads(request.data), type, country, player)


@app.route('/predict/last-goal/<type>/country/<country>/<player>',  methods=['POST'])
def predict_last_goal(type, country, player):
    print(request.data)

    return player_score_last_prediction.predict(json.loads(request.data), type, country, player)



# need to also schedule this -- this is for me to get it started.
@app.route('/train/results', methods=['POST'])
def train_results():
    match_result_train.train()

    return "Done"

# need to also schedule this -- this is for me to get it started.
@app.route('/train/scores', methods=['POST'])
def train_scores():
    match_score_train.train()

    return "Done"


# need to also schedule this -- this is for me to get it started.
@app.route('/train/goals', methods=['POST'])
def train_goals():
    player_goals_train.train()

    return "Done"

# need to also schedule this -- this is for me to get it started.
@app.route('/train/goals/<type>/<country>/<player>', methods=['POST'])
def train_player_goals(type, country, player):
    player_goals_train.train_player(type, country,player)

    return "Done"

# need to also schedule this -- this is for me to get it started.
@app.route('/train/score-first', methods=['POST'])
def train_to_score_first():
    player_score_first_train.train()

    return "Done"

# need to also schedule this -- this is for me to get it started.
@app.route('/train/score-first/<type>/<country>/<player>', methods=['POST'])
def train_player_to_score_first(type, country, player):
    player_score_first_train.train_player(type, country, player)

    return "Done"

# need to also schedule this -- this is for me to get it started.
@app.route('/train/score-last', methods=['POST'])
def train_to_score_last():
    player_score_last_train.train()

    return "Done"

# need to also schedule this -- this is for me to get it started.
@app.route('/train/score-last/<type>/<country>/<player>', methods=['POST'])
def train_player_to_score_last(type, country, player):
    player_score_last_train.train_player(type, country, player)

    return "Done"
