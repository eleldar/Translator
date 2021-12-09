# Translator

## Описание
Переводчик на основе библиотеки marian-nmt. Написан на чистом C ++ ([статья](http://www.aclweb.org/anthology/P18-4020)). 
Основной зависимостью Marian является Boost (собрание библиотек классов, использующих функциональность языка C++ и предоставляющих удобный кроссплатформенный высокоуровневый интерфейс для лаконичного кодирования различных повседневных подзадач программирования); должно быть в системе до работы с marian-nmt.
Marian быть скомпилирован на машинах с устройствами NVIDIA GPU и CUDA 8.0+ или на машинах с CPU. Версия Marian для ЦП компилируется автоматически, если обнаружены OpenBLAS или Intel MKL (рекомендуется). Компиляцию на GPU или CPU можно отключить (в примере ниже отключается GPU).

## Установка
Есть два основных репозитория в github, из которых можно получить marian:

- [последний стабильный выпуск](https://github.com/marian-nmt/marian)
- [репозиторий, поддерживаемый разработчиками этой библиотеки](https://github.com/marian-nmt/marian-dev).
Для релизной версии следует при компиляции использовать флаг ```-DCMAKE_BUILD_TYPE=Release```. 

### Linux

#### c GPU
...

#### без GPU
```
$ sudo git clone https://github.com/marian-nmt/marian
$ wget -qO- 'https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB' | sudo apt-key add -
$ sudo sh -c 'echo deb https://apt.repos.intel.com/mkl all main > /etc/apt/sources.list.d/intel-mkl.list'
$ sudo apt update
$ sudo apt install intel-mkl-64bit-2020.0-088
$ sudo kdir marian/build
$ cd marian/build
$ sudo cmake .. -DCOMPILE_CPU=on -DCOMPILE_CUDA=off
$ sudo make -j[число доступных процессоров]
```

### Windows
#### c GPU
...

#### без GPU
...

## Модели
Для перевода требуются модели, которые могут быть получены 3 основными способами:
- скачать готовые модели
- обучить на своих данных
- дообучение гипотетически возможно, но решение пока неоднозначно!

### Типы моделей
...

### Источники моделей
- трансформеры проектов OPUS, размещенные в [репозитории huggingface](https://huggingface.co/Helsinki-NLP).
  На этом ресурсе доступны модели двух проектов по машинному переводу:
  ([Opus-MT](https://github.com/Helsinki-NLP/Opus-MT)
  и [Tatoeba](https://tatoeba.org/ru/)).
  Проект Opus-MT ориентирован на предоставление инструментов и моделей для перевода, 
  а Tatoeba - на формирование корпусов текстов для перевода (в т.ч. несколько моделей языковых пар).
  Список доступных моделей проекта Opus-MT получен с использованием скрипта в notebook.ipynb.
- обучить с помощью команды [marian](https://marian-nmt.github.io/docs/)
- дообучить предобученные [модели](https://huggingface.co/transformers/model_doc/marian.html).



## Перевод
- В папке examples запустите скрипт ```get_data.sh```, который подгрузит исходные данные (более 200 Мб).
Перейдите в папку ```examples/simple_translation/``` и выполните скрипт ```translate.sh``` для перевода или используйте команду:
``` 
~/marian/build/marian-decoder -m model.npz -v vocab.spm < data/input.en vocab.spm > output.de
```
Эта команда переводит предложения из файла input.en (содержит предварительно обработанные предложения)
в файл output.de (содержит такие же разметки, как и в файле input.en);
здесь используется модель model.npz (RNN) и бинарный словарь vocab.spm (получается в результате обучения).
- ...

## Обучение
...

## Наборы данных
- [Tatoeba Challenge Data](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/data)
- ...

## Дообучение
...
