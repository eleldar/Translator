#!/bin/sh
if ! [ -d ./model/ ]
then
  mkdir model
  wget https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ara/opus+bt-2021-04-13.zip
  unzip opus+bt-2021-04-13.zip -d ./model/
  rm opus+bt-2021-04-13.zip
       https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ara/opus+bt-2021-04-13.zip
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
