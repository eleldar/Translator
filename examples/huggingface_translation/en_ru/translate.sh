#!/bin/sh
SPM=./data/source.spm
DECODER=./marian-dev/build/marian-decoder 
VOCAB=./model/opus.spm32k-spm32k.vocab.yml
MODEL=./model/opus.spm32k-spm32k.transformer-align.model1.npz.best-perplexity.npz
./preprocess.sh _ ${SPM} < $1 |
${DECODER} -m ${MODEL} -v ${VOCAB} ${VOCAB} | 
./postprocess.sh 
