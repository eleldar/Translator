import os
import torch
from .tools.preprocess import get_commands, preprocess_text
from transformers import MarianMTModel, MarianTokenizer
from sentence_splitter import SentenceSplitter, split_text_into_sentences

device = 'cuda:0' if torch.cuda.is_available() else 'cpu'

model = MarianMTModel.from_pretrained
tokenizer = MarianTokenizer.from_pretrained

# Translation models path
local_path = os.path.join('models', 'translation')
remote_path = 'Helsinki-NLP'
remote_prefix = 'opus-mt'

# Check and make translation model directory
if not (os.path.exists(local_path) and os.path.isdir(local_path)):
    os.makedirs(local_path, exist_ok=True)

directs = {'en-ru', 
           'ar-ru',
           'ru-ar',
           'ru-en',
           'en-ar',
           'ar-en',
}

# Languages dictionary and saved translation local models
languages = {}
for direct in directs:
    local_dir = os.path.join(local_path, direct)
    try:
        languages[direct] = {'model': model(local_dir), 'tokenizer': tokenizer(local_dir)}
    except:
        remote_dir = '/'.join([remote_path, f'{remote_prefix}-{direct}'])
        remote_model = model(remote_dir)
        remote_tokinizer =  tokenizer(remote_dir)
        languages[direct] = {'model': remote_model, 'tokenizer': remote_tokinizer} 
        remote_model.save_pretrained(local_dir)
        remote_tokinizer.save_pretrained(local_dir)
   

# словарь команд для предобработки на основе файла с расширением направления перевода и checkpoints
commands = get_commands(directs)

no_split_languages = {'ar'} # языки, предложения для которых нельзя разбить
prefix_languages = {'ar': '>>ara<< '} # мультиязычные словари


def translate(model, tokenizer, direct, text):
    '''перевод одного предложения'''
    text = preprocess_text(commands[direct], text) if direct in commands else text
    input_ids = tokenizer(text, return_tensors="pt").to(device)
    model = model.to(device)
    output_ids = model.generate(**input_ids)[0]
    output = tokenizer.decode(output_ids, skip_special_tokens=True)
    return output


def get_sentences(direct, text):
    '''обработка нескольких предложений'''
    src = languages[direct]
    model, tokenizer = src['model'], src['tokenizer']
    text = text.replace('\n', ' ')
    result = []
    source, target = direct.split('-')
    prefix = prefix_languages[target] if target in prefix_languages else ''
    if source not in no_split_languages:
        for sent in split_text_into_sentences(text, language=source):
            result.append(translate(model, tokenizer, direct, sent))
    else:
        for sent in text.split('.'):
            if sent:
                sent = prefix + sent
                result.append(translate(model, tokenizer, direct, sent))
    return " ".join(result)


if __name__ == '__main__':
    text = get_sentences('en-ru', 'Hello, world')
    print(text)

