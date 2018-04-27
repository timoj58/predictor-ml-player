import tensorflow as tf

def create(feature_columns):
    # Build 2 hidden layer DNN with 10, 10 units respectively.  (from example will enrich at some point).
    return tf.estimator.DNNClassifier(
        feature_columns=feature_columns,
        # Two hidden layers of 10 nodes each.
        hidden_units=[10, 10],
        # The model must choose between 3 classes.
        n_classes=3)

