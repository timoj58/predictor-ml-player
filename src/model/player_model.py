import dataset.player_dataset as player_dataset
import featureset.player_featureset as player_featureset
import util.vocab_utils as vocab_utils
import util.classifier_utils as classifier_utils
import util.dataset_utils as dataset_utils
import util.model_utils as model_utils


def create(type, country, player, train, label, label_values, model_dir, file_type, convert):

    if convert:
        convertValue = label_values
    else:
        convertValue = convert

    (train_x, train_y), (test_x, test_y) = player_dataset.load_data(
        model_utils.MODEL_RES_DIR+'train-'+file_type+type+'-'+country+'-'+player+'.csv',
        model_utils.MODEL_RES_DIR+'test-'+file_type+type+'-'+country+'-'+player+'.csv',
        label, convertValue)

    print ('player vocab started...')
    teamCount = vocab_utils.create_vocab(vocab_utils.TEAMS_URL, vocab_utils.TEAMS_FILE, type, country);
    print ('player vocab completed')
    print ('team vocab started...')
    playerCount = vocab_utils.create_vocab(vocab_utils.PLAYERS_URL,vocab_utils.PLAYERS_FILE, type, country);
    print ('team vocab completed')

    # and the other numerics.  they will be read from a CSV / or direct from mongo more likely.  yes.  from mongo.
    # and review checkpoints, to only train with the newest data?  or build from scratch.  lets see.
    #need to add the label field too.

    feature_columns = player_featureset.create_feature_columns(
        vocab_utils.PLAYERS_FILE+"-"+type+"-"+country+".txt",
        playerCount,
        vocab_utils.TEAMS_FILE+"-"+type+"-"+country+".txt",
        teamCount)


    # Build 2 hidden layer DNN with 10, 10 units respectively.  (from example will enrich at some point).
    classifier = classifier_utils.create(feature_columns,len(label_values), model_utils.MODELS_DIR+model_dir+'/'+type+'/'+country+'/'+player)

    if train:
        # Train the Model.
        classifier.train(
            input_fn=lambda:dataset_utils.train_input_fn(train_x, train_y,50),steps=1000)

        # Evaluate the model.
        eval_result = classifier.evaluate(
            input_fn=lambda:dataset_utils.eval_input_fn(test_x, test_y,50))

        print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))


    return classifier








