import tensorflow as tf
from util.config_utils import get_dir_cfg


def create_vocab_column(key, vocab):

    return tf.feature_column.indicator_column(
        tf.feature_column.categorical_column_with_vocabulary_list(
           key=key,
           vocabulary_list=vocab))


def create_category_indicator_column(key, filename):

    return tf.feature_column.indicator_column(
        tf.feature_column.categorical_column_with_vocabulary_file(
            key=key,
            vocabulary_file=filename,
            vocabulary_size=None))


def create_category_column(key, filename):

    return tf.feature_column.categorical_column_with_vocabulary_file(
        key=key,
        vocabulary_file=filename,
        vocabulary_size=None)

def create_home_players(player_vocab, learning_cfg):

 home_player1_fc = create_category_column('homePlayer1', player_vocab)
 home_player2_fc = create_category_column('homePlayer2', player_vocab)
 home_player3_fc = create_category_column('homePlayer3', player_vocab)
 home_player4_fc = create_category_column('homePlayer4', player_vocab)
 home_player5_fc = create_category_column('homePlayer5', player_vocab)
 home_player6_fc = create_category_column('homePlayer6', player_vocab)
 home_player7_fc = create_category_column('homePlayer7', player_vocab)
 home_player8_fc = create_category_column('homePlayer8', player_vocab)
 home_player9_fc = create_category_column('homePlayer9', player_vocab)
 home_player10_fc = create_category_column('homePlayer10', player_vocab)
 home_player11_fc = create_category_column('homePlayer11', player_vocab)
 home_sub1_fc = create_category_column('homeSub1', player_vocab)
 home_sub2_fc = create_category_column('homeSub2', player_vocab)
 home_sub3_fc = create_category_column('homeSub3', player_vocab)

 # Cross the bucketized columns, using 5000 hash bins.
 return tf.feature_column.crossed_column(
    [home_player1_fc, home_player2_fc, home_player3_fc,home_player4_fc,
     home_player5_fc,home_player6_fc,home_player7_fc,home_player8_fc,
     home_player9_fc,home_player10_fc,home_player11_fc,
     home_sub1_fc, home_sub2_fc, home_sub3_fc], learning_cfg['hash_bins'])



def create_away_players(player_vocab, learning_cfg):

 away_player1_fc = create_category_column('awayPlayer1', player_vocab)
 away_player2_fc = create_category_column('awayPlayer2', player_vocab)
 away_player3_fc = create_category_column('awayPlayer3', player_vocab)
 away_player4_fc = create_category_column('awayPlayer4', player_vocab)
 away_player5_fc = create_category_column('awayPlayer5', player_vocab)
 away_player6_fc = create_category_column('awayPlayer6', player_vocab)
 away_player7_fc = create_category_column('awayPlayer7', player_vocab)
 away_player8_fc = create_category_column('awayPlayer8', player_vocab)
 away_player9_fc = create_category_column('awayPlayer9', player_vocab)
 away_player10_fc = create_category_column('awayPlayer10', player_vocab)
 away_player11_fc = create_category_column('awayPlayer11', player_vocab)
 away_sub1_fc = create_category_column('awaySub1', player_vocab)
 away_sub2_fc = create_category_column('awaySub2', player_vocab)
 away_sub3_fc = create_category_column('awaySub3', player_vocab)

 # Cross the bucketized columns, using 5000 hash bins.
 return tf.feature_column.crossed_column(
    [away_player1_fc, away_player2_fc, away_player3_fc,away_player4_fc,
     away_player5_fc,away_player6_fc,away_player7_fc,away_player8_fc,
     away_player9_fc,away_player10_fc,away_player11_fc,
     away_sub1_fc,away_sub2_fc,away_sub3_fc], learning_cfg['hash_bins'])


def create_teams(team_vocab):

    home = create_category_column('home', team_vocab)
    away = create_category_column('away', team_vocab)

    return tf.feature_column.crossed_column(
        [home, away], 5000)


