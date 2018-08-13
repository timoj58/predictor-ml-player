import dataset.match_dataset as match_dataset
import featureset.match_featureset as match_featureset
import util.vocab_utils as vocab_utils
import util.classifier_utils as classifier_utils
import util.dataset_utils as dataset_utils
from util.file_utils import on_finish
from util.file_utils import clear_directory
from util.config_utils import get_dir_cfg

import logging
import os.path
import json


logger = logging.getLogger(__name__)
local_dir = get_dir_cfg()['local']

def create(type, country, train, label, label_values, model_dir, test_filename, train_filename, outcome):

    aws_model_dir = 'models/'+model_dir+'/'+type+'/'+country
    tf_models_dir = local_dir+'/'+aws_model_dir

    logger.info('team vocab started...')
    team_file = vocab_utils.create_vocab(vocab_utils.TEAMS_URL, vocab_utils.TEAMS_FILE, type, country, None);
    logger.info('team vocab completed')
    logger.info ('player vocab started...')
    player_file = vocab_utils.create_vocab(vocab_utils.PLAYERS_BY_COUNTRY_URL,vocab_utils.PLAYERS_BY_COUNTRY_FILE, type, country, None);
    logger.info ('player vocab completed')

    # and the other numerics.  they will be read from a CSV / or direct from mongo more likely.  yes.  from mongo.
    # and review checkpoints, to only train with the newest data?  or build from scratch.  lets see.
    #need to add the label field too.

    feature_columns = match_featureset.create_feature_columns(player_file, team_file, outcome)

    # Build 2 hidden layer DNN with 10, 10 units respectively.  (from example will enrich at some point).
    classifier = classifier_utils.create(feature_columns,len(label_values), aws_model_dir)

    if train:

        (train_x, train_y), (test_x, test_y) = match_dataset.load_data(
            local_dir+train_filename,
            local_dir+test_filename,
            label, label_values)

        # Train the Model.
        classifier.train(
            input_fn=lambda:dataset_utils.train_input_fn(train_x, train_y,len(train_y)),steps=get_dir_cfg()['steps'])

        # Evaluate the model.   not much use anymore.  but could use the first test file.  makes sense
        eval_result = classifier.evaluate(
            input_fn=lambda:dataset_utils.eval_input_fn(test_x, test_y,get_dir_cfg()['batch_size']))

        logger.info('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

        if get_dir_cfg()['aws_debug']:
         with open(local_dir+'sample.json') as f:
          sample = json.load(f)

         predict(classifier, sample, label_values)

        tidy_up(tf_models_dir, aws_model_dir, team_file, train_filename)


    return classifier

def tidy_up(tf_models_dir, aws_model_dir, team_file, train_filename):
    #probably can tidy this all up.  in one call.
    if aws_model_dir is not None:
     on_finish(tf_models_dir, aws_model_dir)
    else:
     clear_directory(tf_models_dir)
    #also get rid of the vocab files and training / testing files.
    #vocab
    if team_file is not None:
     clear_directory(os.path.dirname(team_file))
    #training
    if train_filename is not None:
     clear_directory(os.path.dirname(local_dir+train_filename))


def predict(classifier, predict_x, label_values):
      logger.info('predict data '+json.dumps(predict_x))
      predictions = classifier.predict(
        input_fn=lambda: dataset_utils.eval_input_fn(predict_x,
                                                     labels=None,
                                                     batch_size=1))
      template = ('\nPrediction is "{}" ({:.1f}%)')

      response = {}

      for pred_dict in predictions:
       class_id = pred_dict['class_ids'][0]
       #probability = pred_dict['probabilities'][class_id]

       index = 0
       for probability in pred_dict['probabilities'] :
        #probability = pred_dict['probabilities'][class_id]
        item = {}
        item['label'] = label_values[index]
        item['score'] = '{:.1f}'.format(100 * probability)

        response[index] = item
        logger.info(template.format(label_values[index],
                               100 * probability))

        index += 1

      return response







