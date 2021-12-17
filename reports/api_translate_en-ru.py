#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import requests
from sentence_splitter import SentenceSplitter, split_text_into_sentences
import time
sourceid="en"
targetid="ru"
source = f'input.{sourceid}'
target = f'api-output.en-{targetid}'
url = 'http://localhost:8080/Translation/Translate' 
headers = {'accept': 'application/json',
           'Content-Type': 'application/json',
}
with open(source, encoding='utf-8') as f:
    text = f.readlines()
text = (" ".join([i.strip() for i in text]))
text = split_text_into_sentences(text, language=sourceid)
if os.path.exists(target):
    os.remove(target)
result = []
n = 0
for sent in text:
    n += 1
    sent = sent.encode('latin-1', 'ignore').decode("utf-8")
    print(n, sent[:50], end='...')
    data = '{\n  "text": "' + sent + '",\n  "sourceLanguage": "' + sourceid + '",\n  "targetLanguage": "' + targetid + '"\n}'
    response = requests.post(url, headers=headers, data=data)
    answer = response.text[1:-5]
    print(answer[:50])
    result.append(answer)
    time.sleep(1)
with open(target, 'w', encoding='utf-8') as f:
    f.write("\n".join(result) + '\n')
