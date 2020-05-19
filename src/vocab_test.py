import util.vocab_utils as vocab_utils
import train.player_goals_train as train

#vocab_utils.create_vocab(
#    url='http://ec2-34-229-85-188.compute-1.amazonaws.com:8090/api/prediction/players/by-country-dict',
#    filename='test.txt',
#    type='FOOTBALL',
#    country='england',
#    player_id=None,
#    previous_vocab_date='2018-30-11'
#)

vocab_utils.patch_vocab(
    '/home/timmytime/IdeaProjects/predictor-ml-model/res/new_file.txt',
    '/home/timmytime/IdeaProjects/predictor-ml-model/res/previous_file.txt',
    [{ 'id': 'a test'},{'id':'i should be added'}, { 'id': 'a new test'},{'id': 'and somemore' }]
    )



