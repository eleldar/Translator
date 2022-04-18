#!/bin/sh
if ! [ -d ./model/ ]
then
  mkdir model
  wget https://object.pouta.csc.fi/Tatoeba-MT-models/sem-eng/opus4m+btTCv20210807-2021-10-01.zip
  unzip opus4m+btTCv20210807-2021-10-01.zip -d ./model/ 
  rm opus4m+btTCv20210807-2021-10-01.zip
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
