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




def main(argv):

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

  # Generate predictions from the model
 expected = [0,1,2]
 predict_x = {
        'home': ['d4a0297e-05db-42cd-af91-30a2e8bc887c','d4a0297e-05db-42cd-af91-30a2e8bc887c','d4a0297e-05db-42cd-af91-30a2e8bc887c'],
        'homePlayer1': ['a070685b-b38f-4e72-8ba5-895828e77abf','a070685b-b38f-4e72-8ba5-895828e77abf','a070685b-b38f-4e72-8ba5-895828e77abf'],
        'homePlayer2': ['066249dc-0fa5-4c68-b719-ed073c406409','066249dc-0fa5-4c68-b719-ed073c406409','066249dc-0fa5-4c68-b719-ed073c406409'],
        'homePlayer3': ['1bc563f8-0dd7-4952-89f3-92d3206a17d2','1bc563f8-0dd7-4952-89f3-92d3206a17d2','1bc563f8-0dd7-4952-89f3-92d3206a17d2'],
        'homePlayer4': ['f2d83175-e6af-4b0a-9b22-e8734ffafca0','f2d83175-e6af-4b0a-9b22-e8734ffafca0','f2d83175-e6af-4b0a-9b22-e8734ffafca0'],
        'homePlayer5': ['5f0fb093-8eaa-43af-8c23-7d1936cb4f8e','5f0fb093-8eaa-43af-8c23-7d1936cb4f8e','5f0fb093-8eaa-43af-8c23-7d1936cb4f8e'],
        'homePlayer6': ['dd546fa2-1a32-4377-a9ea-f65b15bac150','dd546fa2-1a32-4377-a9ea-f65b15bac150','dd546fa2-1a32-4377-a9ea-f65b15bac150'],
        'homePlayer7': ['831ef8c3-12d4-42da-aaaa-dd72855bc472','831ef8c3-12d4-42da-aaaa-dd72855bc472','831ef8c3-12d4-42da-aaaa-dd72855bc472'],
        'homePlayer8': ['cc7d56c3-7fcc-4d27-8bba-aa4f42de4ffc','cc7d56c3-7fcc-4d27-8bba-aa4f42de4ffc','cc7d56c3-7fcc-4d27-8bba-aa4f42de4ffc'],
        'homePlayer9': ['0a2ef70b-5e76-4803-913e-597d1d9d819b','0a2ef70b-5e76-4803-913e-597d1d9d819b','0a2ef70b-5e76-4803-913e-597d1d9d819b'],
        'homePlayer10': ['46bb4880-71c3-44b9-95ea-0a0cbf05809b','46bb4880-71c3-44b9-95ea-0a0cbf05809b','46bb4880-71c3-44b9-95ea-0a0cbf05809b'],
        'homePlayer11': ['bc115d52-4197-4c78-8a2f-286624d501f2','bc115d52-4197-4c78-8a2f-286624d501f2','bc115d52-4197-4c78-8a2f-286624d501f2'],
        'homeSub1': ['d4b77fde-5f7e-440f-8a97-13d40109a337','d4b77fde-5f7e-440f-8a97-13d40109a337','d4b77fde-5f7e-440f-8a97-13d40109a337'],
        'homeSub2': ['ff4e9833-a1b0-4584-bb6d-e72b0f530cf0','ff4e9833-a1b0-4584-bb6d-e72b0f530cf0','ff4e9833-a1b0-4584-bb6d-e72b0f530cf0'],
        'homeSub3': ['352a0eef-5b2d-446a-8167-b28ba0f5a6a5','352a0eef-5b2d-446a-8167-b28ba0f5a6a5','352a0eef-5b2d-446a-8167-b28ba0f5a6a5'],
        'away': ['0a64c5c2-108b-4f61-b270-d4c420e5b3d4','0a64c5c2-108b-4f61-b270-d4c420e5b3d4','0a64c5c2-108b-4f61-b270-d4c420e5b3d4'],
        'awayPlayer1': ['e1a0e1a7-9a67-47f0-9297-8c7818096dce','e1a0e1a7-9a67-47f0-9297-8c7818096dce','e1a0e1a7-9a67-47f0-9297-8c7818096dce'],
        'awayPlayer2': ['7f635732-f0e0-428f-9960-a631471b2a04','7f635732-f0e0-428f-9960-a631471b2a04','6350ffd7-28ec-4615-be77-b1905a4dfd6d'],
        'awayPlayer3': ['6350ffd7-28ec-4615-be77-b1905a4dfd6d','6350ffd7-28ec-4615-be77-b1905a4dfd6d','7f635732-f0e0-428f-9960-a631471b2a04'],
        'awayPlayer4': ['46392ee7-eea4-440e-879a-090e67759692','46392ee7-eea4-440e-879a-090e67759692','46392ee7-eea4-440e-879a-090e67759692'],
        'awayPlayer5': ['fffdd0a3-493f-4e48-899c-3c4372092589','fffdd0a3-493f-4e48-899c-3c4372092589','fffdd0a3-493f-4e48-899c-3c4372092589'],
        'awayPlayer6': ['3d31f7dd-587e-435f-b2ff-2fd9aeeff45c','3d31f7dd-587e-435f-b2ff-2fd9aeeff45c','3d31f7dd-587e-435f-b2ff-2fd9aeeff45c'],
        'awayPlayer7': ['b5785992-29cf-490a-b840-28952fd5c388','b5785992-29cf-490a-b840-28952fd5c388','b5785992-29cf-490a-b840-28952fd5c388'],
        'awayPlayer8': ['b2a2a38f-30ae-4d3e-aad3-bcf59e679ff2','b2a2a38f-30ae-4d3e-aad3-bcf59e679ff2','b2a2a38f-30ae-4d3e-aad3-bcf59e679ff2'],
        'awayPlayer9': ['a0c3421a-0395-4f32-b7d6-7aa39e50cb78','a0c3421a-0395-4f32-b7d6-7aa39e50cb78','a0c3421a-0395-4f32-b7d6-7aa39e50cb78'],
        'awayPlayer10': ['a3a4169f-a833-4eae-a039-d9764c4ea9f0','a3a4169f-a833-4eae-a039-d9764c4ea9f0','a3a4169f-a833-4eae-a039-d9764c4ea9f0'],
        'awayPlayer11': ['378c0da8-5eee-48dc-ab90-8a7ef5c0c413','378c0da8-5eee-48dc-ab90-8a7ef5c0c413','378c0da8-5eee-48dc-ab90-8a7ef5c0c413'],
        'awaySub1': ['c6b6e505-a993-4544-a3de-2ef21cbeac96','c6b6e505-a993-4544-a3de-2ef21cbeac96','c6b6e505-a993-4544-a3de-2ef21cbeac96'],
        'awaySub2': ['f58ffc97-161e-4de8-9ca5-280c25c92100','f58ffc97-161e-4de8-9ca5-280c25c92100','f58ffc97-161e-4de8-9ca5-280c25c92100'],
        'awaySub3': ['57bf89fb-0866-4dad-a74c-b31bd3a3f477','57bf89fb-0866-4dad-a74c-b31bd3a3f477','57bf89fb-0866-4dad-a74c-b31bd3a3f477'],
        'homeWin': [3.0,3.0,2.9],
        'awayWin':[2.0,2.2,3.0],
        'draw':[1.0,1.0,1.0]
    }

 predictions = classifier.predict(
        input_fn=lambda:match_result_dataset.eval_input_fn(predict_x,
                                                labels=None,
                                                batch_size=100))

 template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

 for pred_dict, expec in zip(predictions, expected):
        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        print(template.format(match_result_dataset.OUTCOMES[class_id],
                              100 * probability, expec))
   

if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)











