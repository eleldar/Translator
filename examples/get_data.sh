#!/bin/sh
wget http://data.statmt.org/romang/marian-examples/marian-tutorial-mtm19.tgz
tar zxvf marian-tutorial-mtm19.tgz
cp marian-tutorial-mtm19/1_decoding/data/newstest2014.de ./simple_translation/data/input.de
cp marian-tutorial-mtm19/1_decoding/data/newstest2014.en ./simple_translation/data/input.en
cp marian-tutorial-mtm19/1_decoding/model.npz ./simple_translation/
rm marian-tutorial-mtm19.tgz
rm -rf marian-tutorial-mtm19
