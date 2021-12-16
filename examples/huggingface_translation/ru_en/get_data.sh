#!/bin/sh
if ! [ -d ./model/ ]
then
  mkdir model
  wget https://object.pouta.csc.fi/Tatoeba-MT-models/zle-eng/opus1m+bt-2021-05-02.zip
  unzip opus1m+bt-2021-05-02.zip -d ./model/
  rm opus1m+bt-2021-05-02.zip
fi
if ! [ -d ./tools/ ]
then
  ln -s ~/ ./tools
fi
if ! [ -d ./mosesdecoder/ ]
then
  mkdir -p mosesdecoder/tmp
  git clone https://github.com/marian-nmt/marian-examples.git ./mosesdecoder/tmp
  cd ./mosesdecoder/tmp/tools/
  make
  mv ./moses-scripts/scripts ../..
  rm -rf ../../tmp
fi
