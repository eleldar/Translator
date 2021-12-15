#!/bin/bash
lang="en"
text=""
while read line
do
  text+="${line} "
done
python3 - << EOF
text = " ".join("""$text""".split('\n '))
from sentence_splitter import SentenceSplitter, split_text_into_sentences
result = ("\n".join((split_text_into_sentences(text, language="$lang"))))
with open('src.tmp', 'w', encoding='utf-8') as f:
    f.write(f"{result}\n")
EOF
SPM=./model/source.spm
DECODER=./marian-dev/build/marian-decoder 
VOCAB=./model/opus.spm32k-spm32k.vocab.yml
MODEL=./model/opus.spm32k-spm32k.transformer-align.model1.npz.best-perplexity.npz
./model/preprocess.sh _ ${SPM} < ./src.tmp |
${DECODER} -m ${MODEL} -v ${VOCAB} ${VOCAB} | 
./model/postprocess.sh 
rm ./src.tmp
