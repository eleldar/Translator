import os
import torch
from .tools.preprocess import get_commands, preprocess_text
from transformers import MarianMTModel, MarianTokenizer
from sentence_splitter import SentenceSplitter, split_text_into_sentences
import time
import psutil

model = MarianMTModel.from_pretrained
tokenizer = MarianTokenizer.from_pretrained

# директория models
if not (os.path.exists('models') and os.path.isdir('models')):
    os.mkdir('models')
directory = 'models' if os.listdir('models') else 'Helsinki-NLP'

checkpoints = {
    'en-ru': f'{directory}/opus-mt-en-ru', 
    'ar-ru': f'{directory}/opus-mt-ar-ru',
    'ru-ar': f'{directory}/opus-mt-ru-ar',
    'ru-en': f'{directory}/opus-mt-ru-en',
    'en-ar': f'{directory}/opus-mt-en-ar',
    'ar-en': f'{directory}/opus-mt-ar-en',
}


# словарь моделей на основе checkpoints
languages = {cp: {'model': model(checkpoints[cp]), 'tokenizer': tokenizer(checkpoints[cp])} for cp in checkpoints}

# словарь команд для предобработки на основе файла с расширением направления перевода и checkpoints
commands = get_commands(checkpoints)

no_split_languages = {'ar'} # языки, предложения для которых нельзя разбить
prefix_languages = {'ar': '>>ara<< '} # мультиязычные словари


def translate(model, tokenizer, direct, text):
    '''перевод одного предложения'''
    memory_start = psutil.Process().memory_info().rss
    preproc = time.time()
    text = preprocess_text(commands[direct], text) if direct in commands else text
    preproc = time.time() - preproc

    token = time.time()
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    token = time.time() - token

    generate = time.time()
    output_ids = model.generate(input_ids)[0]
    generate = time.time() - generate

    decode = time.time()
    output = tokenizer.decode(output_ids, skip_special_tokens=True)
    decode = time.time() - decode 
    memory_end = psutil.Process().memory_info().rss

    return output, {
                    'preproc': preproc, 'token': token, 'generate': generate, 'decode': decode, 
                    'memory_start': memory_start, 'memory_end': memory_end
                   }


def get_sentences(direct, text):
    '''обработка нескольких предложений'''
    src = languages[direct]
    model, tokenizer = src['model'], src['tokenizer']
    text = text.replace('\n', ' ')
    resources = {
            'preproc': 0, 'token': 0, 'generate': 0, 'decode': 0, 
            'memory_start': [], 'memory_end': []
    }
    result = []
    response = None
    source, target = direct.split('-')
    prefix = prefix_languages[target] if target in prefix_languages else ''
    if source not in no_split_languages:
        for sent in split_text_into_sentences(text, language=source):
            sent = prefix + sent
            response = translate(model, tokenizer, direct, sent)
            result.append(response[0])
            resources['preproc'] += response[1]['preproc'] 
            resources['token'] += response[1]['token'] 
            resources['generate'] += response[1]['generate'] 
            resources['decode'] += response[1]['decode'] 
            resources['memory_start'].append(response[1]['memory_start'])
            resources['memory_end'].append(response[1]['memory_end'])

    else:
        for sent in text.split('.'):
            if sent:
                sent = prefix + sent
                response = translate(model, tokenizer, direct, sent)
                result.append(response[0])
                resources['preproc'] += response[1]['preproc'] 
                resources['token'] += response[1]['token'] 
                resources['generate'] += response[1]['generate'] 
                resources['decode'] += response[1]['decode'] 
                resources['memory_start'].append(response[1]['memory_start'])
                resources['memory_end'].append(response[1]['memory_end'])

    resources['memory_start'] = sum(resources['memory_start']) / len(resources['memory_start'])
    resources['memory_end'] = sum(resources['memory_end']) / len(resources['memory_end'])
    resources['memory'] = resources['memory_end'] - resources['memory_start']
#    del resources['memory_start']
#    del resources['memory_end']
    return " ".join(result), resources


if __name__ == '__main__':
    text = get_sentences('en-ru', 'Hello, world')
    print(text)

