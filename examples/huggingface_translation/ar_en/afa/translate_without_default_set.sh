#!/bin/bash
read
SPM=./model/source.spm
DECODER=./marian-dev/build/marian-decoder 
VOCAB=./model/opus4m.spm32k-spm32k.vocab.yml
MODEL=./model/opus4m.spm32k-spm32k.transformer.model1.npz.best-perplexity.npz
#echo ">>ara<< ${REPLY}" | # c этим префиксом некоторые предложения переводились лучше, однако в мануале этого нет 
echo ${REPLY} | 
./model/preprocess.sh _ ${SPM} |
${DECODER} -m ${MODEL} -v ${VOCAB} ${VOCAB} | 
./model/postprocess.sh 
