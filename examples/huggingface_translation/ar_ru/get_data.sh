#!/bin/sh
if ! [ -d ./model/ ]
then
  mkdir model
  wget https://object.pouta.csc.fi/Tatoeba-MT-models/ara-rus/opus-2021-02-23.zip
  unzip opus-2021-02-23.zip -d ./model/ 
  rm opus-2021-02-23.zip
fi
if ! [ -d ./marian-dev/ ]
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
