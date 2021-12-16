#!/bin/bash
read
SPM=./model/source.spm
DECODER=./tools/marian-dev/build/marian-decoder 
VOCAB=./model/opus4m+btTCv20210807.spm32k-spm32k.vocab.yml
MODEL=./model/opus4m+btTCv20210807.spm32k-spm32k.transformer.model1.npz.best-perplexity.npz
LANDID='eng'
echo ${REPLY} | 
./model/preprocess.sh _ ${LANDID} ${SPM} |
${DECODER} -m ${MODEL} -v ${VOCAB} ${VOCAB} | 
./model/postprocess.sh 
