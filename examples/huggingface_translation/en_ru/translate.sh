#!/bin/bash
text=""
while read line
do
  text+="${line} "
done
python3 - << EOF
from sentence_splitter import SentenceSplitter, split_text_into_sentences
result = ("\n".join((split_text_into_sentences("$text", language='en'))))
with open('src.tmp', 'w', encoding='utf-8') as f:
    f.write(f"{result}\n")
EOF
SPM=./data/source.spm
DECODER=./marian-dev/build/marian-decoder 
VOCAB=./model/opus.spm32k-spm32k.vocab.yml
MODEL=./model/opus.spm32k-spm32k.transformer-align.model1.npz.best-perplexity.npz
./preprocess.sh _ ${SPM} < ./src.tmp |
${DECODER} -m ${MODEL} -v ${VOCAB} ${VOCAB} | 
./postprocess.sh 
rm ./src.tmp
