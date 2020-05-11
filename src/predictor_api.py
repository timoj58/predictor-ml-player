from flask import Flask
from flask import request
import predict.player_goals_prediction as player_goals_prediction
import predict.player_assists_prediction as player_assists_prediction
import predict.player_saves_prediction as player_saves_prediction
import predict.player_minutes_prediction as player_minutes_prediction
import predict.player_conceded_prediction as player_conceded_prediction

import train.player_saves_train as player_saves_train
import train.player_goals_train as player_goals_train
import train.player_assists_train as player_assists_train
import train.player_minutes_train as player_minutes_train
import train.player_conceded_train as player_conceded_train
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



@app.route('/predict/goals/<player>/<receipt>',  methods=['POST'])
def predict_goals(player, receipt):
    thread = threading.Thread(target=player_goals_prediction.predict,
                              args=(json.loads(request.data), player, receipt))
    process(thread)

    return json.dumps(done_response())


@app.route('/predict/saves/<player>/<receipt>',  methods=['POST'])
def predict_saves(player, receipt):
    thread = threading.Thread(target=player_saves_prediction.predict,
                              args=(json.loads(request.data), player, receipt))
    process(thread)

    return json.dumps(done_response())


@app.route('/predict/assists/<player>/<receipt>',  methods=['POST'])
def predict_assists(player, receipt):
    thread = threading.Thread(target=player_assists_prediction.predict,
                              args=(json.loads(request.data), player, receipt))
    process(thread)

    return json.dumps(done_response())


@app.route('/predict/minutes/<player>/<receipt>',  methods=['POST'])
def predict_minutes(player, receipt):
    thread = threading.Thread(target=player_minutes_prediction.predict,
                              args=(json.loads(request.data), player, receipt))
    process(thread)

    return json.dumps(done_response())


@app.route('/predict/conceded/<player>/<receipt>',  methods=['POST'])
def predict_conceded(player, receipt):
    thread = threading.Thread(target=player_conceded_prediction.predict,
                              args=(json.loads(request.data), player, receipt))
    process(thread)

    return json.dumps(done_response())


# need to also schedule this -- this is for me to get it started.
@app.route('/train/conceded/<player>/<receipt>', methods=['POST'])
def train_goals_conceded(player, receipt):
    thread = threading.Thread(target=player_conceded_train.train,
                              args=(player, receipt))
    process(thread)

    return json.dumps(done_response())

@app.route('/train/goals/<player>/<receipt>', methods=['POST'])
def train_goals_scored(player, receipt):
    thread = threading.Thread(target=player_goals_train.train,
                              args=(player, receipt))
    process(thread)

    return json.dumps(done_response())

@app.route('/train/saves/<player>/<receipt>', methods=['POST'])
def train_saves(player, receipt):
    thread = threading.Thread(target=player_saves_train.train,
                              args=(player, receipt))
    process(thread)

    return json.dumps(done_response())

@app.route('/train/assists/<player>/<receipt>', methods=['POST'])
def train_assists(player, receipt):
    thread = threading.Thread(target=player_assists_train.train,
                              args=(player, receipt))
    process(thread)

    return json.dumps(done_response())

@app.route('/train/minutes/<player>/<receipt>', methods=['POST'])
def train_minutes(player, receipt):
    thread = threading.Thread(target=player_minutes_train.train,
                              args=(player, receipt))
    process(thread)

    return json.dumps(done_response())
