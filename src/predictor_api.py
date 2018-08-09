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
from util.config_utils import get_dir_cfg

import json
import logging
import threading

app = Flask(__name__)

logging.basicConfig(filename=get_dir_cfg()['local']+'predictor.log',level=logging.INFO)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

# should handle errors at some point
def done_response():
    item = {}
    item['status'] = 'Done'
    return item

@app.route('/info')
def test_app():
    return json.dumps(done_response())


@app.route('/predict/result/<type>/<country>/<receipt>',  methods=['POST'])
def predict_result(type, country, receipt):
    print(request.data)

    return match_result_prediction.predict(json.loads(request.data), type, country)

@app.route('/predict/score/<type>/<country>/<receipt>',  methods=['POST'])
def predict_score(type, country,receipt):
    print(request.data)

    return match_score_prediction.predict(json.loads(request.data), type, country)


@app.route('/predict/goals/<type>/<country>/<player>/<receipt>',  methods=['POST'])
def predict_goals_player(type, country, player, receipt):
    print(request.data)

    return player_goals_prediction.predict(json.loads(request.data), type, country, player)


@app.route('/predict/first-goal/<type>/<country>/<player>/<receipt>',  methods=['POST'])
def predict_first_goal(type, country, player, receipt):
    print(request.data)

    return player_score_first_prediction.predict(json.loads(request.data), type, country, player)


@app.route('/predict/last-goal/<type>/<country>/<player>/<receipt>',  methods=['POST'])
def predict_last_goal(type, country, player, receipt):
    print(request.data)

    return player_score_last_prediction.predict(json.loads(request.data), type, country, player)



# need to also schedule this -- this is for me to get it started.
@app.route('/train/results/<receipt>', methods=['POST'])
def train_results(receipt):
    thread = threading.Thread(target=match_result_train.train,
                              args=(receipt))
    thread.start()

    return json.dumps(done_response())


# need to also schedule this -- this is for me to get it started.
@app.route('/train/results/<type>/<country>/<receipt>', methods=['POST'])
def train_country_results(type, country, receipt):
    thread = threading.Thread(target=match_result_train.train_country,
                          args=(type, country, receipt))
    thread.start()

    return json.dumps(done_response())

# need to also schedule this -- this is for me to get it started.
@app.route('/train/scores/<receipt>', methods=['POST'])
def train_scores(receipt):
    thread = threading.Thread(target=match_score_train.train,
                              args=(receipt))
    thread.start()

    return json.dumps(done_response())


# need to also schedule this -- this is for me to get it started.
@app.route('/train/scores/<type>/<country>/<receipt>', methods=['POST'])
def train_country_scores(type, country, receipt):
    thread = threading.Thread(target=match_score_train.train_country,
                              args=(type, country, receipt))
    thread.start()

    return json.dumps(done_response())

# need to also schedule this -- this is for me to get it started.
@app.route('/train/goals/<receipt>', methods=['POST'])
def train_goals(receipt):
    thread = threading.Thread(target=player_goals_train.train,
                              args=(receipt))
    thread.start()

    return json.dumps(done_response())

# need to also schedule this -- this is for me to get it started.
@app.route('/train/goals/<type>/<country>/<player>/<receipt>', methods=['POST'])
def train_player_goals(type, country, player, receipt):
    thread = threading.Thread(target=player_goals_train.train_player,
                              args=(type, country,player, receipt))
    thread.start()

    return json.dumps(done_response())

# need to also schedule this -- this is for me to get it started.
@app.route('/train/score-first/<receipt>', methods=['POST'])
def train_to_score_first(receipt):
    thread = threading.Thread(target=player_score_first_train.train,
                              args=(receipt))
    thread.start()

    return json.dumps(done_response())

# need to also schedule this -- this is for me to get it started.
@app.route('/train/score-first/<type>/<country>/<player>/<receipt>', methods=['POST'])
def train_player_to_score_first(type, country, player, receipt):
    thread = threading.Thread(target=player_score_first_train.train_player,
                              args=(type, country, player, receipt))
    thread.start()

    return json.dumps(done_response())

# need to also schedule this -- this is for me to get it started.
@app.route('/train/score-last/<receipt>', methods=['POST'])
def train_to_score_last(receipt):
    thread = threading.Thread(target=player_score_last_train.train,
                              args=(receipt))
    thread.start()

    return json.dumps(done_response())

# need to also schedule this -- this is for me to get it started.
@app.route('/train/score-last/<type>/<country>/<player>/<receipt>', methods=['POST'])
def train_player_to_score_last(type, country, player, receipt):
    thread = threading.Thread(target=player_score_last_train.train_player,
                              args=(type, country, player, receipt))
    thread.start()

    return json.dumps(done_response())
