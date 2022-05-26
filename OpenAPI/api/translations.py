import os
import sys
import torch
from pathlib import Path
from contextlib import redirect_stdout
from transformers import MarianMTModel, MarianTokenizer
from sentence_splitter import SentenceSplitter, split_text_into_sentences

# Language translation settings
directs = {'en-ru', 
           'ar-ru',
           'ru-ar',
           'ru-en',
           'en-ar',
           'ar-en',
}
no_split_languages = {'ar'} # языки, предложения для которых нельзя разбить
prefix_languages = {'ar': '>>ara<< '} # мультиязычные словари

# Source translation models for hf.co
remote_path = 'Helsinki-NLP'
remote_prefix = 'opus-mt'

# Device settings
device = 'cuda:0' if torch.cuda.is_available() else 'cpu'

# Local path settings
drive, path_and_file = os.path.splitdrive(Path(__file__).absolute())
path, file = os.path.split(path_and_file)
curdir = os.path.join(drive, path)

# Import tools
sys.path.append(curdir)
from tools.preprocess import get_commands, text_preprocess, sent_preprocess
commands = get_commands(directs)

# Models settings
model = MarianMTModel.from_pretrained
tokenizer = MarianTokenizer.from_pretrained
local_path = os.path.join(curdir, 'models', 'translation')
if not (os.path.exists(local_path) and os.path.isdir(local_path)):
    os.makedirs(local_path, exist_ok=True)
languages = {}
for direct in directs:
    local_dir = os.path.join(local_path, direct)
    try:
        languages[direct] = {'model': model(local_dir), 'tokenizer': tokenizer(local_dir)}
        print(f'Used local {direct} model from: {local_dir}')
    except:
        remote_dir = '/'.join([remote_path, f'{remote_prefix}-{direct}'])
        print(f'Not local {direct} model and it will be download from: {remote_dir}')
        remote_model = model(remote_dir)
        remote_tokinizer =  tokenizer(remote_dir)
        languages[direct] = {'model': remote_model, 'tokenizer': remote_tokinizer} 
        remote_model.save_pretrained(local_dir)
        remote_tokinizer.save_pretrained(local_dir)


def sent_translation(model, tokenizer, direct, text):
    '''перевод одного предложения'''
    text = sent_preprocess(commands[direct], text) if direct in commands else text
    input_ids = tokenizer(text, return_tensors="pt").to(device)
    model = model.to(device)
    output_ids = model.generate(**input_ids)[0]
    output = tokenizer.decode(output_ids, skip_special_tokens=True)
    return output


def translate(direct, text):
    '''обработка нескольких предложений'''
    text = text_preprocess(text)
    src = languages[direct]
    model, tokenizer = src['model'], src['tokenizer']
    result = []
    source, target = direct.split('-')
    prefix = prefix_languages[target] if target in prefix_languages else ''
    if source not in no_split_languages:
        sents = split_text_into_sentences(text, language=source)
    else:
        sents = text.split('.')
    for sent in sents:
        if sent:
            sent = prefix + sent
            result.append(sent_translation(model, tokenizer, direct, sent))
    return " ".join(result)


if __name__ == '__main__':
    text = translate('en-ru', 'Hello, world')
    print(text)

print('Using GPU' if device == 'cuda:0' else 'Using only CPU')
print('Preprocess commands is ok' if commands else 'Not found preprocess commands')
