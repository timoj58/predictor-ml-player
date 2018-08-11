import util.vocab_utils as vocab_utils

vocab_utils.patch_vocab(
    '/home/timmytime/IdeaProjects/predictor-ml-model/res/new_file.txt',
    '/home/timmytime/IdeaProjects/predictor-ml-model/res/previous_file.txt',
    [{ 'id': 'a test'},{ 'id': 'a new test'},{'id': 'and somemore' }, {'id':'i should be added'}]
    )
