import os
import sys
from pathlib import Path
from transformers import pipeline
from sentence_splitter import SentenceSplitter, split_text_into_sentences

# Language translation settings
directs = ['en-ru',]

# Local path settings
drive, path_and_file = os.path.splitdrive(Path(__file__).absolute())
path, file = os.path.split(path_and_file)
curdir = os.path.join(drive, path)

# Import tools
sys.path.append(curdir)
from tools.preprocess import get_commands, text_preprocess, sent_preprocess
from tools.prestarter import examples
from tools.language_detection import sent_detection
commands = get_commands(directs)

# Models settings
direct = directs[0]
local_dir = os.path.join(curdir, 'models', 'translation', direct)
model = pipeline('translation', local_dir)
sent_translation = lambda sent: model(sent)[0]['translation_text']


def translate(direct, text):
    '''обработка нескольких предложений'''
    text = text_preprocess(text)
    result = []
    source, target = direct.split('-')
    sents = split_text_into_sentences(text, language=source)
    for sent in sents:
        if sent and sent_detection(sent, direct):
            result.append(sent_translation(sent))
        elif sent:
            result.append(sent)
    return " ".join(result)


def prestart(directs):
    print('-' * 50)
    print('Prestarted track:')
    result = {}
    for direct in directs:
        result[direct] = []
        for example in examples(direct):
            result[direct].append(True if translate(direct, example) else False)
        print(f'Direct {direct} successfully prestarted {len(result[direct])} sentences' if result[direct] else f'Prestart direct {direct} is bad')
    print('Result: ', end='')
    return {key: len(value) for key, value in result.items()}


if __name__ == '__main__':
    text = translate('en-ru', 'Hello, world')
    print(text)


print('-' * 50)
print('Preprocess commands is ok' if commands else 'Not found preprocess commands')
print('Prestart is ok' if all(i for i in prestart(directs).values()) else 'Some prestart directs are not made')
