from flask import Flask, request
from flask_restful import Resource, Api
import torch
from transformers import MarianMTModel, MarianTokenizer
from sentence_splitter import SentenceSplitter, split_text_into_sentences

languages = {
        'en-ru': {'model': MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-ru'),
                  'tokenizer': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-ru')},
        'ar-ru': {'model': MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-ar-ru'),
                  'tokenizer': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-ar-ru')},
        'ru-ar': {'model': MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-ru-ar'),
                  'tokenizer': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-ru-ar')},
        'ru-en': {'model': MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-ru-en'),
                  'tokenizer': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-ru-en')},
        'en-ar': {'model': MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-ar'),
                  'tokenizer': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-ar')},
        'ar-en': {'model': MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-ar-en'),
                  'tokenizer': MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-ar-en')},
} 

no_split_languages = {'ar'} # языки, предложения для которых нельзя разбить
prefix_languages = {'ar': '>>ara<< '} # мультиязычные словари

app = Flask(__name__)
api = Api(app)


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


class Translation(Resource):
    '''обработчик RESTful запросов'''
    def get(self):
        result = dict(request.form)
        try:
            text = result['source']
            direct = result['direct']
            result['target'] = get_sentences(direct, text)
            return result, 200
        except KeyError:
            return {'get example': "data={'direct': 'en-ru', 'source': 'Hello, World!'}"}, 404

api.add_resource(Translation, '/api', '/api/')

if __name__ == '__main__':
    app.run(debug=True)







