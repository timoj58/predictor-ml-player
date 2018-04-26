import tensorflow as tf

def create_category_column(key, filename, filesize):

 return tf.feature_column.indicator_column(
         tf.feature_column.categorical_column_with_vocabulary_file(
         key=key,
         vocabulary_file=filename,
         vocabulary_size=filesize))

def create_feature_columns(player_vocab, player_vocab_count, team_vocab, team_vocab_count):
 # sort out the featulre columns
 feature_columns = []
 
 feature_columns.append(create_category_column('home', team_vocab, team_vocab_count))

 feature_columns.append(create_category_column('homePlayer1', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('homePlayer2', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('homePlayer3', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('homePlayer4', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('homePlayer5', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('homePlayer6', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('homePlayer7', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('homePlayer8', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('homePlayer9', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('homePlayer10', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('homePlayer11', player_vocab, player_vocab_count))

 feature_columns.append(create_category_column('homeSub1', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('homeSub2', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('homeSub3', player_vocab, player_vocab_count))

 feature_columns.append(create_category_column('away', team_vocab, team_vocab_count))

 feature_columns.append(create_category_column('awayPlayer1', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('awayPlayer2', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('awayPlayer3', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('awayPlayer4', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('awayPlayer5', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('awayPlayer6', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('awayPlayer7', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('awayPlayer8', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('awayPlayer9', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('awayPlayer10', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('awayPlayer11', player_vocab, player_vocab_count))

 feature_columns.append(create_category_column('awaySub1', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('awaySub2', player_vocab, player_vocab_count))
 feature_columns.append(create_category_column('awaySub3', player_vocab, player_vocab_count))

 feature_columns.append(tf.feature_column.numeric_column(key='homeWin'))
 feature_columns.append(tf.feature_column.numeric_column(key='awayWin'))
 feature_columns.append(tf.feature_column.numeric_column(key='draw'))

 return feature_columns;


