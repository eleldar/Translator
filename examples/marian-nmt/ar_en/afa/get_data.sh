#!/bin/sh
if ! [ -d ./model/ ]
then
  mkdir model
  wget https://object.pouta.csc.fi/Tatoeba-MT-models/afa-eng/opus4m-2020-08-12.zip
  unzip opus4m-2020-08-12.zip -d ./model/ 
  rm opus4m-2020-08-12.zip
fi
if ! [ -d ./marian-dev/ ]
then
  ln -s ~/marian-dev ./marian-dev
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
