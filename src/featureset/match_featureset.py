import tensorflow as tf
import util.featureset_utils as featureset_utils
import dataset.match_dataset as match_dataset


def create_feature_columns(player_vocab, player_vocab_count, team_vocab, team_vocab_count, outcome):
 # sort out the featulre columns
 feature_columns = []
 
 feature_columns.append(featureset_utils.create_category_indicator_column('home', team_vocab, team_vocab_count))

 feature_columns.append(tf.feature_column.indicator_column(featureset_utils.create_home_players(player_vocab, player_vocab_count)))

 feature_columns.append(tf.feature_column.indicator_column(featureset_utils.create_home_subs(player_vocab, player_vocab_count)))

 feature_columns.append(featureset_utils.create_category_indicator_column('away', team_vocab, team_vocab_count))

 feature_columns.append(tf.feature_column.indicator_column(featureset_utils.create_away_players(player_vocab, player_vocab_count)))

 feature_columns.append(tf.feature_column.indicator_column(featureset_utils.create_away_subs(player_vocab, player_vocab_count)))

 if outcome:
  feature_columns.append(featureset_utils.create_vocab_column('outcome', match_dataset.OUTCOMES))

 return feature_columns


