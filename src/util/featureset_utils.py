import tensorflow as tf


def create_category_indicator_column(key, filename, filesize):

    return tf.feature_column.indicator_column(
        tf.feature_column.categorical_column_with_vocabulary_file(
            key=key,
            vocabulary_file=filename,
            vocabulary_size=filesize))


def create_category_column(key, filename, filesize):

    return tf.feature_column.categorical_column_with_vocabulary_file(
        key=key,
        vocabulary_file=filename,
        vocabulary_size=filesize)

def create_home_players(player_vocab, player_vocab_count):

 home_player1_fc = create_category_column('homePlayer1', player_vocab, player_vocab_count)
 home_player2_fc = create_category_column('homePlayer2', player_vocab, player_vocab_count)
 home_player3_fc = create_category_column('homePlayer3', player_vocab, player_vocab_count)
 home_player4_fc = create_category_column('homePlayer4', player_vocab, player_vocab_count)
 home_player5_fc = create_category_column('homePlayer5', player_vocab, player_vocab_count)
 home_player6_fc = create_category_column('homePlayer6', player_vocab, player_vocab_count)
 home_player7_fc = create_category_column('homePlayer7', player_vocab, player_vocab_count)
 home_player8_fc = create_category_column('homePlayer8', player_vocab, player_vocab_count)
 home_player9_fc = create_category_column('homePlayer9', player_vocab, player_vocab_count)
 home_player10_fc = create_category_column('homePlayer10', player_vocab, player_vocab_count)
 home_player11_fc = create_category_column('homePlayer11', player_vocab, player_vocab_count)

 # Cross the bucketized columns, using 5000 hash bins.
 return tf.feature_column.crossed_column(
    [home_player1_fc, home_player2_fc, home_player3_fc,home_player4_fc,
     home_player5_fc,home_player6_fc,home_player7_fc,home_player8_fc,
     home_player9_fc,home_player10_fc,home_player11_fc], 5000)


def create_home_subs(player_vocab, player_vocab_count):

 home_sub1_fc = create_category_column('homeSub1', player_vocab, player_vocab_count)
 home_sub2_fc = create_category_column('homeSub2', player_vocab, player_vocab_count)
 home_sub3_fc = create_category_column('homeSub3', player_vocab, player_vocab_count)

 # Cross the bucketized columns, using 5000 hash bins.
 return tf.feature_column.crossed_column(
    [home_sub1_fc, home_sub2_fc, home_sub3_fc], 5000)

def create_away_players(player_vocab, player_vocab_count):

 away_player1_fc = create_category_column('awayPlayer1', player_vocab, player_vocab_count)
 away_player2_fc = create_category_column('awayPlayer2', player_vocab, player_vocab_count)
 away_player3_fc = create_category_column('awayPlayer3', player_vocab, player_vocab_count)
 away_player4_fc = create_category_column('awayPlayer4', player_vocab, player_vocab_count)
 away_player5_fc = create_category_column('awayPlayer5', player_vocab, player_vocab_count)
 away_player6_fc = create_category_column('awayPlayer6', player_vocab, player_vocab_count)
 away_player7_fc = create_category_column('awayPlayer7', player_vocab, player_vocab_count)
 away_player8_fc = create_category_column('awayPlayer8', player_vocab, player_vocab_count)
 away_player9_fc = create_category_column('awayPlayer9', player_vocab, player_vocab_count)
 away_player10_fc = create_category_column('awayPlayer10', player_vocab, player_vocab_count)
 away_player11_fc = create_category_column('awayPlayer11', player_vocab, player_vocab_count)

 # Cross the bucketized columns, using 5000 hash bins.
 return tf.feature_column.crossed_column(
    [away_player1_fc, away_player2_fc, away_player3_fc,away_player4_fc,
     away_player5_fc,away_player6_fc,away_player7_fc,away_player8_fc,
     away_player9_fc,away_player10_fc,away_player11_fc], 5000)



def create_away_subs(player_vocab, player_vocab_count):

 away_sub1_fc = create_category_column('awaySub1', player_vocab, player_vocab_count)
 away_sub2_fc = create_category_column('awaySub2', player_vocab, player_vocab_count)
 away_sub3_fc = create_category_column('awaySub3', player_vocab, player_vocab_count)

 # Cross the bucketized columns, using 5000 hash bins.
 return tf.feature_column.crossed_column(
    [away_sub1_fc, away_sub2_fc, away_sub3_fc], 5000)

