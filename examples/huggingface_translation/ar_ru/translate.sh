#!/bin/bash
read
SPM=./model/source.spm
DECODER=./tools/marian-dev/build/marian-decoder 
SET=./model/decoder.yml
#echo ">>ara<< ${REPLY}" | # c этим префиксом некоторые предложения переводились лучше, однако в мануале этого нет
echo "${REPLY}" | 
./model/preprocess.sh _ ${SPM} |
${DECODER} -c ${SET} | ./model/postprocess.sh 
