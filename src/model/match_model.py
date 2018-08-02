import dataset.match_dataset as match_dataset
import featureset.match_featureset as match_featureset
import util.vocab_utils as vocab_utils
import util.classifier_utils as classifier_utils
import util.dataset_utils as dataset_utils
import util.model_utils as model_utils
from util.file_utils import on_finish


def create(type, country, train, label, label_values, model_dir, file_type, outcome):

    aws_model_dir = +type+'/'+country
    tf_models_dir = model_utils.MODELS_DIR+model_dir+'/'+aws_model_dir

    (train_x, train_y), (test_x, test_y) = match_dataset.load_data(
        model_utils.MODEL_RES_DIR+'train-'+file_type+type+'-'+country+'.csv',
        model_utils.MODEL_RES_DIR+'test-'+file_type+type+'-'+country+'.csv',
        label, label_values)

    print ('team vocab started...')
    team_file = vocab_utils.create_vocab(vocab_utils.TEAMS_URL, vocab_utils.TEAMS_FILE, type, country, None);
    print ('team vocab completed')
    print ('player vocab started...')
    player_file = vocab_utils.create_vocab(vocab_utils.PLAYERS_BY_COUNTRY_URL,vocab_utils.PLAYERS_BY_COUNTRY_FILE, type, country, None);
    print ('player vocab completed')

    # and the other numerics.  they will be read from a CSV / or direct from mongo more likely.  yes.  from mongo.
    # and review checkpoints, to only train with the newest data?  or build from scratch.  lets see.
    #need to add the label field too.

    feature_columns = match_featureset.create_feature_columns(player_file, team_file, outcome)

    # Build 2 hidden layer DNN with 10, 10 units respectively.  (from example will enrich at some point).
    classifier = classifier_utils.create(feature_columns,len(label_values), tf_models_dir)

    if train:


        print(len(train_y))
        # Train the Model.
        classifier.train(
            input_fn=lambda:dataset_utils.train_input_fn(train_x, train_y,len(train_y)),steps=1000)

        # Evaluate the model.   not much use anymore.  but could use the first test file.  makes sense
        eval_result = classifier.evaluate(
            input_fn=lambda:dataset_utils.eval_input_fn(test_x, test_y,50))

        print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    #probably can tidy this all up.  in one call.
    on_finish(tf_models_dir, aws_model_dir)


    return classifier








