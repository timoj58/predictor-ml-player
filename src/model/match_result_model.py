import tensorflow as tf
import requests
from requests.auth import HTTPDigestAuth
import json
import dataset.match_result_dataset as match_result_dataset
import featureset.match_result_featureset as match_result_featureset

TEAMS_URL = "http://localhost:8090/api/prediction/teams"
PLAYERS_URL = "http://localhost:8090/api/prediction/players"


def create_vocab(url, filename):
 
  response = requests.get(url)
  values = response.json()

  size = 0
  
  with open(filename, 'w') as f:
   for value in values:
     label = value['id']
     if label is not None:
       f.write(label.encode('unicode_escape')) 
       f.write('\n')
       size += 1

  return size




def create():

 (train_x, train_y), (test_x, test_y) = match_result_dataset.load_data(
                        '/home/timmytime/IdeaProjects/predictor-ml-model/res/train.csv', 
                        '/home/timmytime/IdeaProjects/predictor-ml-model/res/train.csv')

 teamCount = create_vocab(TEAMS_URL, '/home/timmytime/IdeaProjects/predictor-ml-model/res/team-vocab.txt');
 playerCount = create_vocab(PLAYERS_URL, '/home/timmytime/IdeaProjects/predictor-ml-model/res/player-vocab.txt');

 print('team count {} player count {}'.format(teamCount, playerCount))


 # and the other numerics.  they will be read from a CSV / or direct from mongo more likely.  yes.  from mongo.
 # and review checkpoints, to only train with the newest data?  or build from scratch.  lets see.
 #need to add the label field too.

 feature_columns = match_result_featureset.create_feature_columns(
    '/home/timmytime/IdeaProjects/predictor-ml-model/res/player-vocab.txt',
    playerCount,
    '/home/timmytime/IdeaProjects/predictor-ml-model/res/team-vocab.txt',
    teamCount)

 # Build 2 hidden layer DNN with 10, 10 units respectively.  (from example will enrich at some point).
 classifier = tf.estimator.DNNClassifier(
        feature_columns=feature_columns,
        # Two hidden layers of 10 nodes each.
        hidden_units=[10, 10],
        # The model must choose between 3 classes.
        n_classes=3)
 
 # Train the Model.
 classifier.train(
        input_fn=lambda:match_result_dataset.train_input_fn(train_x, train_y,100),steps=1000)

 # Evaluate the model.
 eval_result = classifier.evaluate(
        input_fn=lambda:match_result_dataset.eval_input_fn(test_x, test_y,100))

 print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

 return classifier











