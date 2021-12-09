#!/bin/sh
# выводит оценку переведенного текста в файле output.de
# в сравнении с переводом input.de
score/multi-bleu.perl data/input.de < output.de
# расскоментируйте следующую строку для получения аналогичного результата
#cat output.de | score/multi-bleu.perl data/input.de
