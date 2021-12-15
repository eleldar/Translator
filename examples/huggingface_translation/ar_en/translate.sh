#!/bin/bash
read
SPM=./model/source.spm
DECODER=./tools/marian-dev/build/marian-decoder 
SET=./model/decoder.yml
echo ">>ara<< ${REPLY}" | ./model/preprocess.sh _ ${SPM} |
${DECODER} -c ${SET} | ./model/postprocess.sh 
