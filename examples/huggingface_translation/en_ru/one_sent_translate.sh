#!/bin/bash
read MESSAGE
SPM=./data/source.spm
DECODER=./marian-dev/build/marian-decoder 
VOCAB=./model/opus.spm32k-spm32k.vocab.yml
MODEL=./model/opus.spm32k-spm32k.transformer-align.model1.npz.best-perplexity.npz
echo "$MESSAGE" | ./preprocess.sh _ ${SPM} |
${DECODER} -m ${MODEL} -v ${VOCAB} ${VOCAB} | 
./postprocess.sh 
