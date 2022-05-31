import os
from langdetect import detect
from pathlib import Path
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification


def sent_detection(sent, direct):
    '''Language ID adaptred for fasttext model'''
    language_id =  detect(sent)
    src_id, _ = direct.split('-')
    return language_id == src_id


if __name__ == '__main__':
    text = 'hello'    
    print(sent_detection(text, 'en-ru'))
