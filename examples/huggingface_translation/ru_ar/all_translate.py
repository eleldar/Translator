#!/bin/python3
import subprocess
import os
from sentence_splitter import SentenceSplitter, split_text_into_sentences

lang="ru"
source = 'input.ru'
target = 'output.ar'
with open(source, encoding='utf-8') as f:
    text = f.readlines()
text = (" ".join([i.strip() for i in text]))
text = split_text_into_sentences(text, language=lang)
if os.path.exists(target):
    os.remove(target)
for sent in text:
    command = f'echo "{sent}" | ./translate.sh >> {target}'
    os.system(command)
