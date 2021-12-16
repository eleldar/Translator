#!/bin/bash
read
SPM=./model/source.spm
DECODER=./tools/marian-dev/build/marian-decoder 
SET=./model/decoder.yml
LANDID='eng'
echo ${REPLY} | 
./model/preprocess.sh _ ${LANDID} ${SPM} |
${DECODER} -c ${SET} | ./model/postprocess.sh 
