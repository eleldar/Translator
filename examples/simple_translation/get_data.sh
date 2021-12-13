#!/bin/sh
wget http://data.statmt.org/romang/marian-examples/marian-tutorial-mtm19.tgz
tar zxvf marian-tutorial-mtm19.tgz
if ! [ -d ./data/ ]
then
  mkdir data
fi
cp marian-tutorial-mtm19/1_decoding/data/newstest2014.de ./data/input.de
cp marian-tutorial-mtm19/1_decoding/data/newstest2014.en ./data/input.en
cp marian-tutorial-mtm19/1_decoding/model.npz ./simple_translation/
rm marian-tutorial-mtm19.tgz
rm -rf marian-tutorial-mtm19
