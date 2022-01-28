import torch
from transformers import MarianMTModel, MarianTokenizer
from sentence_splitter import SentenceSplitter, split_text_into_sentences

model = MarianMTModel.from_pretrained
tokenizer = MarianTokenizer.from_pretrained

checkpoints = {
    'en-ru': 'Helsinki-NLP/opus-mt-en-ru', 
    'ar-ru': 'Helsinki-NLP/opus-mt-ar-ru',
    'ru-ar': 'Helsinki-NLP/opus-mt-ru-ar',
    'ru-en': 'Helsinki-NLP/opus-mt-ru-en',
    'en-ar': 'Helsinki-NLP/opus-mt-en-ar',
    'ar-en': 'Helsinki-NLP/opus-mt-ar-en',
}

languages = {
    'en-ru': {'model': model(checkpoints['en-ru']), 'tokenizer': tokenizer(checkpoints['en-ru'])},
    'ar-ru': {'model': model(checkpoints['ar-ru']), 'tokenizer': tokenizer(checkpoints['ar-ru'])},
    'ru-ar': {'model': model(checkpoints['ru-ar']), 'tokenizer': tokenizer(checkpoints['ru-ar'])},
    'ru-en': {'model': model(checkpoints['ru-en']), 'tokenizer': tokenizer(checkpoints['ru-en'])},
    'en-ar': {'model': model(checkpoints['en-ar']), 'tokenizer': tokenizer(checkpoints['en-ar'])},
    'ar-en': {'model': model(checkpoints['ar-en']), 'tokenizer': tokenizer(checkpoints['ar-en'])},
}

no_split_languages = {'ar'} # языки, предложения для которых нельзя разбить
prefix_languages = {'ar': '>>ara<< '} # мультиязычные словари

def translate(model, tokenizer, direct, text):
    '''перевод одного предложения'''
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