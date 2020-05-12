import tensorflow as tf
import util.featureset_utils as featureset_utils


def create_feature_columns(team_vocab):
 # sort out the featulre columns
 feature_columns = []

 feature_columns.append(featureset_utils.create_category_indicator_column('opponent', team_vocab))
 feature_columns.append(featureset_utils.create_vocab_column('home', ['true', 'false']))

 return feature_columns


