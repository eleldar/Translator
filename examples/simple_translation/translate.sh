#!/bin/sh
# переводит предложения из файла input.en (содержит предварительно обработанные предложения)
# в файл output.de (содержит такие же разметки, как в файле input.en);
# используется модель model.npz (RNN) и словарь vocab.spm
~/marian/build/marian-decoder -m model.npz -v vocab.spm < data/input.en vocab.spm > output.de 
# расскоментируйте следующую строку для получения аналогичного результата
# cat data/input.en | ~/marian/build/marian-decoder -m model.npz -v vocab.spm vocab.spm > output.de 
