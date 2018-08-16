import tensorflow as tf
import util.featureset_utils as featureset_utils
import dataset.match_dataset as match_dataset


def create_feature_columns(player_vocab, team_vocab, outcome, learning_cfg):
 # sort out the featulre columns
 feature_columns = []
 
 feature_columns.append(featureset_utils.create_category_indicator_column('home', team_vocab))

 #feature_columns.append(tf.feature_column.indicator_column(featureset_utils.create_teams(team_vocab)))
 feature_columns.append(tf.feature_column.indicator_column(featureset_utils.create_home_players(player_vocab, learning_cfg)))


 feature_columns.append(featureset_utils.create_category_indicator_column('away', team_vocab))
 feature_columns.append(tf.feature_column.indicator_column(featureset_utils.create_away_players(player_vocab, learning_cfg)))

 if outcome:
  feature_columns.append(featureset_utils.create_vocab_column('outcome', match_dataset.OUTCOMES))

 return feature_columns


