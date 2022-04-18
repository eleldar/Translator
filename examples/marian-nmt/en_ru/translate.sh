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
SET=./model/decoder.yml
./model/preprocess.sh _ ${SPM} < ./src.tmp | ${DECODER} -c ${SET} | ./model/postprocess.sh 
rm ./src.tmp
