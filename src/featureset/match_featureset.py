import tensorflow as tf
import util.featureset_utils as featureset_utils
import dataset.match_dataset as match_dataset


def create_feature_columns(team_vocab, outcome):
 # sort out the featulre columns
 feature_columns = []
 
 feature_columns.append(featureset_utils.create_category_indicator_column('home', team_vocab))
 feature_columns.append(featureset_utils.create_category_indicator_column('away', team_vocab))

 if outcome:
  feature_columns.append(featureset_utils.create_vocab_column('outcome', match_dataset.OUTCOMES))

 return feature_columns


