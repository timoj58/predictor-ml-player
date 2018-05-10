import tensorflow as tf
import model.player_model as player_model
import dataset.player_dataset as player_dataset
import util.dataset_utils as dataset_utils
import util.model_utils as model_utils

def main(argv):

    model_utils.create_csv(model_utils.PLAYER_MODEL_URL+"7f0946e6-cf47-4278-b777-c11f9e485322", "/home/timmytime/IdeaProjects/predictor-ml-model/res/train-player-7f0946e6-cf47-4278-b777-c11f9e485322.csv")


    classifier = player_model.create()

    # Generate predictions from the model
    expected = [0,0,0]
    predict_x = {
        'player':['7f0946e6-cf47-4278-b777-c11f9e485322','7f0946e6-cf47-4278-b777-c11f9e485322','7f0946e6-cf47-4278-b777-c11f9e485322'],
        'home': ['d4a0297e-05db-42cd-af91-30a2e8bc887c','d4a0297e-05db-42cd-af91-30a2e8bc887c','d4a0297e-05db-42cd-af91-30a2e8bc887c'],
        'homePlayer1': ['a070685b-b38f-4e72-8ba5-895828e77abf','a070685b-b38f-4e72-8ba5-895828e77abf','a070685b-b38f-4e72-8ba5-895828e77abf'],
        'homePlayer2': ['066249dc-0fa5-4c68-b719-ed073c406409','066249dc-0fa5-4c68-b719-ed073c406409','066249dc-0fa5-4c68-b719-ed073c406409'],
        'homePlayer3': ['1bc563f8-0dd7-4952-89f3-92d3206a17d2','1bc563f8-0dd7-4952-89f3-92d3206a17d2','1bc563f8-0dd7-4952-89f3-92d3206a17d2'],
        'homePlayer4': ['f2d83175-e6af-4b0a-9b22-e8734ffafca0','f2d83175-e6af-4b0a-9b22-e8734ffafca0','f2d83175-e6af-4b0a-9b22-e8734ffafca0'],
        'homePlayer5': ['5f0fb093-8eaa-43af-8c23-7d1936cb4f8e','5f0fb093-8eaa-43af-8c23-7d1936cb4f8e','5f0fb093-8eaa-43af-8c23-7d1936cb4f8e'],
        'homePlayer6': ['dd546fa2-1a32-4377-a9ea-f65b15bac150','dd546fa2-1a32-4377-a9ea-f65b15bac150','dd546fa2-1a32-4377-a9ea-f65b15bac150'],
        'homePlayer7': ['831ef8c3-12d4-42da-aaaa-dd72855bc472','831ef8c3-12d4-42da-aaaa-dd72855bc472','831ef8c3-12d4-42da-aaaa-dd72855bc472'],
        'homePlayer8': ['cc7d56c3-7fcc-4d27-8bba-aa4f42de4ffc','cc7d56c3-7fcc-4d27-8bba-aa4f42de4ffc','cc7d56c3-7fcc-4d27-8bba-aa4f42de4ffc'],
        'homePlayer9': ['0a2ef70b-5e76-4803-913e-597d1d9d819b','0a2ef70b-5e76-4803-913e-597d1d9d819b','0a2ef70b-5e76-4803-913e-597d1d9d819b'],
        'homePlayer10': ['46bb4880-71c3-44b9-95ea-0a0cbf05809b','46bb4880-71c3-44b9-95ea-0a0cbf05809b','46bb4880-71c3-44b9-95ea-0a0cbf05809b'],
        'homePlayer11': ['bc115d52-4197-4c78-8a2f-286624d501f2','bc115d52-4197-4c78-8a2f-286624d501f2','bc115d52-4197-4c78-8a2f-286624d501f2'],
        'homeSub1': ['d4b77fde-5f7e-440f-8a97-13d40109a337','d4b77fde-5f7e-440f-8a97-13d40109a337','d4b77fde-5f7e-440f-8a97-13d40109a337'],
        'homeSub2': ['ff4e9833-a1b0-4584-bb6d-e72b0f530cf0','ff4e9833-a1b0-4584-bb6d-e72b0f530cf0','352a0eef-5b2d-446a-8167-b28ba0f5a6a5'],
        'homeSub3': ['352a0eef-5b2d-446a-8167-b28ba0f5a6a5','352a0eef-5b2d-446a-8167-b28ba0f5a6a5','ff4e9833-a1b0-4584-bb6d-e72b0f530cf0'],
        'away': ['0a64c5c2-108b-4f61-b270-d4c420e5b3d4','0a64c5c2-108b-4f61-b270-d4c420e5b3d4','0a64c5c2-108b-4f61-b270-d4c420e5b3d4'],
        'awayPlayer1': ['e1a0e1a7-9a67-47f0-9297-8c7818096dce','e1a0e1a7-9a67-47f0-9297-8c7818096dce','e1a0e1a7-9a67-47f0-9297-8c7818096dce'],
        'awayPlayer2': ['7f635732-f0e0-428f-9960-a631471b2a04','7f635732-f0e0-428f-9960-a631471b2a04','6350ffd7-28ec-4615-be77-b1905a4dfd6d'],
        'awayPlayer3': ['6350ffd7-28ec-4615-be77-b1905a4dfd6d','6350ffd7-28ec-4615-be77-b1905a4dfd6d','7f635732-f0e0-428f-9960-a631471b2a04'],
        'awayPlayer4': ['46392ee7-eea4-440e-879a-090e67759692','46392ee7-eea4-440e-879a-090e67759692','46392ee7-eea4-440e-879a-090e67759692'],
        'awayPlayer5': ['fffdd0a3-493f-4e48-899c-3c4372092589','fffdd0a3-493f-4e48-899c-3c4372092589','fffdd0a3-493f-4e48-899c-3c4372092589'],
        'awayPlayer6': ['3d31f7dd-587e-435f-b2ff-2fd9aeeff45c','3d31f7dd-587e-435f-b2ff-2fd9aeeff45c','3d31f7dd-587e-435f-b2ff-2fd9aeeff45c'],
        'awayPlayer7': ['b5785992-29cf-490a-b840-28952fd5c388','b5785992-29cf-490a-b840-28952fd5c388','b5785992-29cf-490a-b840-28952fd5c388'],
        'awayPlayer8': ['b2a2a38f-30ae-4d3e-aad3-bcf59e679ff2','b2a2a38f-30ae-4d3e-aad3-bcf59e679ff2','b2a2a38f-30ae-4d3e-aad3-bcf59e679ff2'],
        'awayPlayer9': ['a0c3421a-0395-4f32-b7d6-7aa39e50cb78','a0c3421a-0395-4f32-b7d6-7aa39e50cb78','a0c3421a-0395-4f32-b7d6-7aa39e50cb78'],
        'awayPlayer10': ['a3a4169f-a833-4eae-a039-d9764c4ea9f0','a3a4169f-a833-4eae-a039-d9764c4ea9f0','a3a4169f-a833-4eae-a039-d9764c4ea9f0'],
        'awayPlayer11': ['378c0da8-5eee-48dc-ab90-8a7ef5c0c413','378c0da8-5eee-48dc-ab90-8a7ef5c0c413','378c0da8-5eee-48dc-ab90-8a7ef5c0c413'],
        'awaySub1': ['c6b6e505-a993-4544-a3de-2ef21cbeac96','c6b6e505-a993-4544-a3de-2ef21cbeac96','c6b6e505-a993-4544-a3de-2ef21cbeac96'],
        'awaySub2': ['f58ffc97-161e-4de8-9ca5-280c25c92100','f58ffc97-161e-4de8-9ca5-280c25c92100','f58ffc97-161e-4de8-9ca5-280c25c92100'],
        'awaySub3': ['57bf89fb-0866-4dad-a74c-b31bd3a3f477','57bf89fb-0866-4dad-a74c-b31bd3a3f477','57bf89fb-0866-4dad-a74c-b31bd3a3f477']
    }

    predictions = classifier.predict(
        input_fn=lambda:dataset_utils.eval_input_fn(predict_x,
                                                    labels=None,
                                                    batch_size=100))

    template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

    for pred_dict, expec in zip(predictions, expected):
        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        print(template.format(player_dataset.GOALS_OUTCOMES[class_id],
                              100 * probability, expec))



if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)

