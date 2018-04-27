import tensorflow as tf
import util.featureset_utils as featureset_utils


def create_feature_columns(player_vocab, player_vocab_count, team_vocab, team_vocab_count, hide):
 # sort out the featulre columns
 feature_columns = []
 
 feature_columns.append(featureset_utils.create_category_indicator_column('home', team_vocab, team_vocab_count))

 feature_columns.append(tf.feature_column.indicator_column(featureset_utils.create_home_players(player_vocab, player_vocab_count)))

 feature_columns.append(tf.feature_column.indicator_column(featureset_utils.create_home_subs(player_vocab, player_vocab_count)))

 feature_columns.append(featureset_utils.create_category_indicator_column('away', team_vocab, team_vocab_count))

 feature_columns.append(tf.feature_column.indicator_column(featureset_utils.create_away_players(player_vocab, player_vocab_count)))

 feature_columns.append(tf.feature_column.indicator_column(featureset_utils.create_away_subs(player_vocab, player_vocab_count)))

 if hide:
  feature_columns.append(tf.feature_column.numeric_column(key='homeWinPrice'))
  feature_columns.append(tf.feature_column.numeric_column(key='awayWinPrice'))
  feature_columns.append(tf.feature_column.numeric_column(key='drawPrice'))

 if not hide:
  feature_columns.append(tf.feature_column.numeric_column(key='correctScorePrice'))


 return feature_columns


