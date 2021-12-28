import torch
from transformers import MarianMTModel, MarianTokenizer
checkpoint = 'Helsinki-NLP/opus-mt-en-ru' # предобученная модель EN-RU

from flask import Flask, escape, request

model = MarianMTModel.from_pretrained(checkpoint)
tokenizer = MarianTokenizer.from_pretrained(checkpoint)

app = Flask(__name__)

@app.route('/')
def hello():
    def translate(text='Hello, World!'):
        input_ids = tokenizer(text, return_tensors="pt").input_ids # Batch size 1
        output_ids = model.generate(input_ids)[0]
        output = tokenizer.decode(output_ids, skip_special_tokens=True)
        return output
    return f"<p>{translate('Security of online payments')}</p>"

