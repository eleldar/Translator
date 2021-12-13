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
