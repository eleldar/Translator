#!/bin/sh
if ! [ -d ./model/ ]
then
  mkdir model
  wget https://object.pouta.csc.fi/OPUS-MT-models/en-ru/opus-2020-02-11.zip
  unzip opus-2020-02-11.zip -d ./model/
  rm opus-2020-02-11.zip
fi
