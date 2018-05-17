import tensorflow as tf

def create(feature_columns, classes, modelDir):
    # Build 2 hidden layer DNN with 10, 10 units respectively.  (from example will enrich at some point).
    return tf.estimator.DNNClassifier(
        feature_columns=feature_columns,
        # Two hidden layers of 10 nodes each. (that was example now changed to 3 layers, need to learn about this more once i have good data
        hidden_units=[64, 32, 16],
        # The model must choose between 3 classes.
        n_classes=classes,
        model_dir=modelDir)

