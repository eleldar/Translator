#!/bin/bash
read
SPM=./model/source.spm
DECODER=./tools/marian-dev/build/marian-decoder 
VOCAB=./model/opus.spm32k-spm32k.vocab.yml
MODEL=./model/opus.spm32k-spm32k.transformer.model1.npz.best-perplexity.npz
echo ${REPLY} | 
./model/preprocess.sh _ ${SPM} |
${DECODER} -m ${MODEL} -v ${VOCAB} ${VOCAB} | 
./model/postprocess.sh 
