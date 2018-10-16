import dataset.player_dataset as player_dataset
import featureset.player_featureset as player_featureset
import util.vocab_utils as vocab_utils
import util.classifier_utils as classifier_utils
import util.dataset_utils as dataset_utils
from util.model_utils import tidy_up
from util.model_utils import predict
from util.config_utils import get_dir_cfg
from util.config_utils import get_learning_cfg

import logging

logger = logging.getLogger(__name__)
local_dir = get_dir_cfg()['local']


def create(type, country, player, train, label, label_values, model_dir, train_filename, test_filename, convert, previous_vocab_date):

    aws_model_dir = 'models/'+model_dir+'/'+type+'/'+country+'/'+player
    tf_models_dir = local_dir+'/'+aws_model_dir

    learning_cfg = get_learning_cfg('player', model_dir)

    if convert:
        convertValue = label_values
    else:
        convertValue = convert


    logger.info ('team vocab started...')
    team_file = vocab_utils.create_vocab(
        url=vocab_utils.TEAMS_URL,
        filename=vocab_utils.TEAMS_FILE,
        type=type,
        country=country,
        player_id=None,
        previous_vocab_date=previous_vocab_date);
    logger.info ('team vocab completed')
    logger.info ('player vocab started...')
    player_file = vocab_utils.create_vocab(
        url=vocab_utils.PLAYERS_URL,
        filename=vocab_utils.PLAYERS_FILE,
        type=type,
        country=country,
        player_id=player,
        previous_vocab_date=previous_vocab_date);
    logger.info ('player vocab completed')

    # and the other numerics.  they will be read from a CSV / or direct from mongo more likely.  yes.  from mongo.
    # and review checkpoints, to only train with the newest data?  or build from scratch.  lets see.
    #need to add the label field too.


    feature_columns = player_featureset.create_feature_columns(
        player_vocab=player_file,
        team_vocab=team_file,
        learning_cfg=learning_cfg)

    #def create(feature_columns, classes, model_dir, learning_cfg):

    # Build 2 hidden layer DNN with 10, 10 units respectively.  (from example will enrich at some point).
    classifier = classifier_utils.create(
        feature_columns=feature_columns,
        classes=len(label_values),
        model_dir=aws_model_dir,
        learning_cfg=learning_cfg)

    if train:
        #def load_data(train_path, test_path, y_name, convert):

        (train_x, train_y), (test_x, test_y) = player_dataset.load_data(
            train_path=local_dir+train_filename,
            test_path=local_dir+test_filename,
            y_name=label,
            convert=convertValue)

        # Train the Model.
        classifier.train(
            input_fn=lambda:dataset_utils.train_input_fn(train_x, train_y, len(train_y)),steps=learning_cfg['steps'])

        # Evaluate the model.  w dont really care about this given we cant set up different data.
        eval_result = classifier.evaluate(
            input_fn=lambda:dataset_utils.eval_input_fn(test_x, test_y,learning_cfg['batch_size']))

        logger.info('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

        if learning_cfg['aws_debug']:
            with open(local_dir+'sample.json') as f:
                sample = json.load(f)

            predict(
                classifier=classifier,
                predict_x=sample,
                label_values=label_values)

        tidy_up(
            tf_models_dir=tf_models_dir,
            aws_model_dir=aws_model_dir,
            team_file=team_file,
            train_filename=train_filename)


    return classifier







