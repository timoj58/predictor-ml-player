from flask import Flask
from flask import request
import predict.match_result_prediction as match_result_prediction
import predict.match_score_prediction as match_score_prediction
import predict.match_goals_prediction as match_goals_prediction
import train.match_result_train as match_result_train
import train.match_score_train as match_score_train
import train.match_goals_train as match_goals_train
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
import traceback

app = Flask(__name__)

logging.basicConfig(filename=get_dir_cfg()['local']+'predictor.log',level=logging.NOTSET)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    app.run(host='0.0.0.0')


##doesnt seem to do anything, should catch interrupted tho.
def process(thread):
    try:
     thread.start()
    except Exception as e:
      logger.error(traceback.format_exc())

# should handle errors at some point
def done_response():
    item = {}
    item['status'] = 'Done'
    return item

@app.route('/info')
def test_app():
    return json.dumps(done_response())



@app.route('/predict/goals/<type>/<country>/<receipt>',  methods=['POST'])
def predict_goals(type, country, receipt):
    thread = threading.Thread(target=match_goals_prediction.predict,
                              args=(json.loads(request.data), type, country, receipt))
    process(thread)

    return json.dumps(done_response())


@app.route('/predict/result/<type>/<country>/<receipt>',  methods=['POST'])
def predict_result(type, country, receipt):
    thread = threading.Thread(target=match_result_prediction.predict,
                              args=(json.loads(request.data), type, country, receipt))
    process(thread)

    return json.dumps(done_response())

@app.route('/predict/score/<type>/<country>/<receipt>',  methods=['POST'])
def predict_score(type, country,receipt):
    thread = threading.Thread(target=match_score_prediction.predict,
                              args=(json.loads(request.data), type, country, receipt))
    process(thread)

    return json.dumps(done_response())


@app.route('/predict/player/goals/<type>/<country>/<player>/<receipt>',  methods=['POST'])
def predict_goals_player(type, country, player, receipt):
    thread = threading.Thread(target=player_goals_prediction.predict,
                              args=(json.loads(request.data), type, country, player, receipt))
    process(thread)

    return json.dumps(done_response())


@app.route('/predict/player/first-goal/<type>/<country>/<player>/<receipt>',  methods=['POST'])
def predict_first_goal(type, country, player, receipt):
    thread = threading.Thread(target=player_score_first_prediction.v,
                              args=(json.loads(request.data), type, country, player, receipt))
    process(thread)

    return json.dumps(done_response())


@app.route('/predict/player/last-goal/<type>/<country>/<player>/<receipt>',  methods=['POST'])
def predict_last_goal(type, country, player, receipt):
    thread = threading.Thread(target=player_score_last_prediction.predict,
                              args=(json.loads(request.data), type, country, player, receipt))
    process(thread)

    return json.dumps(done_response())



# need to also schedule this -- this is for me to get it started.
@app.route('/train/results/<receipt>', methods=['POST'])
def train_results(receipt):
    thread = threading.Thread(target=match_result_train.train,
                              args=(receipt))
    process(thread)

    return json.dumps(done_response())


# need to also schedule this -- this is for me to get it started.
@app.route('/train/results/<type>/<country>/<receipt>', methods=['POST'])
def train_country_results(type, country, receipt):
    thread = threading.Thread(target=match_result_train.train_country,
                          args=(type, country, receipt))
    process(thread)

    return json.dumps(done_response())

# need to also schedule this -- this is for me to get it started.
@app.route('/train/scores/<receipt>', methods=['POST'])
def train_scores(receipt):
    thread = threading.Thread(target=match_score_train.train,
                              args=(receipt))
    process(thread)

    return json.dumps(done_response())


# need to also schedule this -- this is for me to get it started.
@app.route('/train/scores/<type>/<country>/<receipt>', methods=['POST'])
def train_country_scores(type, country, receipt):
    thread = threading.Thread(target=match_score_train.train_country,
                              args=(type, country, receipt))
    process(thread)

    return json.dumps(done_response())



@app.route('/train/goals/<receipt>', methods=['POST'])
def train_total_goals(receipt):
    thread = threading.Thread(target=match_goals_train.train,
                              args=(receipt))
    process(thread)

    return json.dumps(done_response())


# need to also schedule this -- this is for me to get it started.
@app.route('/train/goals/<type>/<country>/<receipt>', methods=['POST'])
def train_country_total_goals(type, country, receipt):
    thread = threading.Thread(target=match_goals_train.train_country,
                              args=(type, country, receipt))
    process(thread)

    return json.dumps(done_response())


# need to also schedule this -- this is for me to get it started.
@app.route('/train/player/goals/<receipt>', methods=['POST'])
def train_goals(receipt):
    thread = threading.Thread(target=player_goals_train.train,
                              args=(receipt))
    process(thread)

    return json.dumps(done_response())

# need to also schedule this -- this is for me to get it started.
@app.route('/train/player/goals/<type>/<country>/<player>/<receipt>', methods=['POST'])
def train_player_goals(type, country, player, receipt):
    thread = threading.Thread(target=player_goals_train.train_player,
                              args=(type, country,player, receipt))
    process(thread)

    return json.dumps(done_response())

# need to also schedule this -- this is for me to get it started.
@app.route('/train/player/score-first/<receipt>', methods=['POST'])
def train_to_score_first(receipt):
    thread = threading.Thread(target=player_score_first_train.train,
                              args=(receipt))
    process(thread)

    return json.dumps(done_response())

# need to also schedule this -- this is for me to get it started.
@app.route('/train/player/score-first/<type>/<country>/<player>/<receipt>', methods=['POST'])
def train_player_to_score_first(type, country, player, receipt):
    thread = threading.Thread(target=player_score_first_train.train_player,
                              args=(type, country, player, receipt))
    process(thread)

    return json.dumps(done_response())

# need to also schedule this -- this is for me to get it started.
@app.route('/train/player/score-last/<receipt>', methods=['POST'])
def train_to_score_last(receipt):
    thread = threading.Thread(target=player_score_last_train.train,
                              args=(receipt))
    process(thread)

    return json.dumps(done_response())

# need to also schedule this -- this is for me to get it started.
@app.route('/train/player/score-last/<type>/<country>/<player>/<receipt>', methods=['POST'])
def train_player_to_score_last(type, country, player, receipt):
    thread = threading.Thread(target=player_score_last_train.train_player,
                              args=(type, country, player, receipt))
    process(thread)

    return json.dumps(done_response())
