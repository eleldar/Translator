#!/bin/sh
NMT=~/marian/build
SPM=./data/source.spm
VOCAB=./model/opus.spm32k-spm32k.vocab.yml
MODEL=./model/opus.spm32k-spm32k.transformer-align.model1.npz.best-perplexity.npz
${NMT}/spm_encode --model ${SPM} $1 |
${NMT}/marian-decoder -m ${MODEL} -v ${VOCAB} ${VOCAB} | ./postprocess.sh 
