#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import requests
from sentence_splitter import SentenceSplitter, split_text_into_sentences
import time
sourceid="ar"
targetid="ru"
source = f'input.{sourceid}'
target = f'api-output.ar-{targetid}'
url = 'http://localhost:8080/Translation/Translate' 
headers = {'accept': 'application/json',
           'Content-Type': 'application/json',
}
result = []
with open(source, encoding='utf-8') as f:
    n = 0
    for i in f:
        sent = i.strip()
        n += 1
        sent = sent.encode('utf-8').decode('latin-1', 'ignore')
        print(n, sent[:50], end='...')
        data = '{\n  "text": "' + str(sent) + '",\n  "sourceLanguage": "' + sourceid + '",\n  "targetLanguage": "' + targetid + '"\n}'
        response = requests.post(url, headers=headers, data=data)
        answer = response.text[1:-5]
        print(answer[:50])
        result.append(answer)
        time.sleep(1)
        
with open(target, 'w', encoding='utf-8') as f:
    f.write("\n".join(result) + '\n')
