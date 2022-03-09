import os
import torch
from .tools.preprocess import get_commands, preprocess_text
from transformers import MarianMTModel, MarianTokenizer
from sentence_splitter import SentenceSplitter, split_text_into_sentences

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
    text = preprocess_text(commands[direct], text) if direct in commands else text
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    output_ids = model.generate(input_ids)[0]
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
            sent = prefix + sent
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

