import tensorflow as tf
import dataset.score_result_dataset as score_result_dataset
import featureset.score_result_featureset as score_result_featureset
import util.vocab_utils as vocab_utils
import util.classifier_utils as classifier_utils
import util.dataset_utils as dataset_utils


def create():

    (train_x, train_y), (test_x, test_y) = score_result_dataset.load_data(
        '/home/timmytime/IdeaProjects/predictor-ml-model/res/train-scores.csv',
        '/home/timmytime/IdeaProjects/predictor-ml-model/res/train-scores.csv')

    teamCount = vocab_utils.create_vocab(vocab_utils.TEAMS_URL, vocab_utils.TEAMS_FILE);
    playerCount = vocab_utils.create_vocab(vocab_utils.PLAYERS_URL, vocab_utils.PLAYERS_FILE);


    # and the other numerics.  they will be read from a CSV / or direct from mongo more likely.  yes.  from mongo.
    # and review checkpoints, to only train with the newest data?  or build from scratch.  lets see.
    #need to add the label field too.

    feature_columns = score_result_featureset.create_feature_columns(
        vocab_utils.PLAYERS_FILE,
        playerCount,
        vocab_utils.TEAMS_FILE,
        teamCount)

    # Build 2 hidden layer DNN with 10, 10 units respectively.  (from example will enrich at some point).
    classifier = classifier_utils.create(feature_columns, len(score_result_dataset.OUTCOMES))

    # Train the Model.
    classifier.train(
        input_fn=lambda:dataset_utils.train_input_fn(train_x, train_y,100),steps=1000)

    # Evaluate the model.
    eval_result = classifier.evaluate(
        input_fn=lambda:dataset_utils.eval_input_fn(test_x, test_y,100))

    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    return classifier











