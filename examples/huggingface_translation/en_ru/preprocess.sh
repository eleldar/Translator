#!/bin/bash
#
# USAGE preprocess.sh langid bpecodes < input > output
#
#
# replace MOSESHOME and SPMENCODE with your own setup! 

SPMENCODE=~/marian/build/spm_encode
TOKENIZER=~/marian/marian-examples/tools/moses-scripts/scripts/tokenizer
SPM=./data/source.spm

cat $1 |
${TOKENIZER}/replace-unicode-punctuation.perl |
${TOKENIZER}/remove-non-printing-char.perl |
sed 's/  */ /g;s/^ *//g;s/ *$//g' |
${SPMENCODE} --model ${SPM}

# ${TOKENIZER}/normalize-punctuation.perl -l $1 |
