import tensorflow as tf
from util.file_utils import get_indexes
from util.file_utils import get_aws_file
from util.config_utils import get_dir_cfg
import logging

logger = logging.getLogger(__name__)


local_dir = get_dir_cfg()['local']


def create(feature_columns, classes, model_dir):

    logger.info ('model dir for classifier '+local_dir+model_dir)

    indexes = get_indexes(local_dir+model_dir)
    for index in indexes:
        get_aws_file(model_dir+'/', index)

    indexes = get_indexes(local_dir+model_dir+'/eval')
    for index in indexes:
        get_aws_file(model_dir+'/eval/', index)


    # Build 2 hidden layer DNN with 10, 10 units respectively.  (from example will enrich at some point).
    return tf.estimator.DNNClassifier(
        feature_columns=feature_columns,
        # Two hidden layers of 10 nodes each. (that was example now changed to 3 layers, need to learn about this more once i have good data
        hidden_units=[1024, 512, 256],
        # The model must choose between 3 classes.
        n_classes=classes,
        model_dir=local_dir+model_dir)

