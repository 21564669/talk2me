import os

ali_qw_key = os.environ.get("ali_qw_key")
audio_stored_path = rf"{os.path.abspath(os.curdir)}{os.sep}audio_result"
audio_model_list = [
    'sambert-beth-v1',
    # 'sambert-betty-v1',
    # 'sambert-cally-v1',
    # 'sambert-cindy-v1',
    # 'sambert-eva-v1',
    # 'sambert-donna-v1',
    # 'sambert-brian-v1'
]