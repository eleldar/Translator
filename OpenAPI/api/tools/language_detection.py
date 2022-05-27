import os
import wget
import fasttext
from pathlib import Path
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification


def create_dir(dir_path):
    '''create dir if it not exists'''
    if not (os.path.exists(dir_path) and os.path.isdir(dir_path)):
        os.makedirs(dir_path, exist_ok=True)


drive, path_and_file = os.path.splitdrive(Path(__file__).absolute())
path, _ = os.path.split(path_and_file)
curdir = os.path.join(drive, path)
local_dir = os.path.join(curdir, '..', 'models', 'classification', 'language-detection')
create_dir(local_dir)


def get_bert_model():
    '''Example for get language id:model(sent)[0]["label"]'''
    bert_dir = os.path.join(local_dir, 'xlm-roberta-base-language-detection')
    create_dir(bert_dir)
    try:
        return pipeline('text-classification', bert_dir)
    except:
        remote_dir = 'eleldar/language-detection'
        remote_model = AutoTokenizer.from_pretrained(remote_dir)
        remote_tokinizer = AutoModelForSequenceClassification.from_pretrained(remote_dir)
        remote_model.save_pretrained(bert_dir)
        remote_tokinizer.save_pretrained(bert_dir)
        return pipeline('text-classification', bert_dir) 


def get_fast_model():
    '''Example for get language id:model(sent)[0][0][-2:]'''
    fast_dir = os.path.join(local_dir, 'fasttext')
    create_dir(fast_dir)
    try:
        return fasttext.load_model(os.path.join(fast_dir, 'lid.176.ftz')).predict
    except:
        remote_dir = 'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz'
        wget.download(remote_dir, out=fast_dir)
        return fasttext.load_model(os.path.join(fast_dir, 'lid.176.ftz')).predict


def sent_detection(sent, direct):
    '''Language ID adaptred for fasttext model'''
    language_id =  model_detection(sent)[0][0][-2:]
    src_id, _ = direct.split('-')
    return language_id == src_id


def text_detection(text, direct):
    '''For future developments'''
    pass

# use only fastext model
model_detection = get_fast_model()

if __name__ == '__main__':
    text = 'hello'    
    print(sent_detection(text, 'en-ru'))
