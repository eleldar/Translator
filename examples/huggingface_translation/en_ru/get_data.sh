#!/bin/sh
if ! [ -d ./model/ ]
then
  mkdir model
  wget https://object.pouta.csc.fi/OPUS-MT-models/en-ru/opus-2020-02-11.zip
  mkdir tmp
  unzip opus-2020-02-11.zip -d ./tmp/
  rm opus-2020-02-11.zip
  mv ./tmp/opus* ./model/
  if ! [ -d ./data/ ]
  then
    mkdir data
    mv ./tmp/*.spm ./data/
  fi
  rm -rf ./tmp/
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
