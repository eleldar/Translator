#!/bin/bash
read 
SPM=./model/source.spm
DECODER=./tools/marian-dev/build/marian-decoder 
VOCAB=./model/opus.spm32k-spm32k.vocab.yml
MODEL=./model/opus.spm32k-spm32k.transformer.model1.npz.best-perplexity.npz
LANDID="ara"
echo ${REPLY} |
./model/preprocess.sh _ ${LANDID} ${SPM} |
${DECODER} -m ${MODEL} -v ${VOCAB} ${VOCAB} | 
./model/postprocess.sh 
