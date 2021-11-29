# Translator

## Описание
Переводчик на основе библиотеки marian-nmt.
Marian написан на чистом C ++ \cite{mariannmt}. 
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
$ mkdir marian/build
$ cd marian/build
$ sudo cmake .. -DCOMPILE_CPU=on -DCOMPILE_CUDA=off
$ make -j[число доступных процессоров]
```

### Windows
#### c GPU
...

#### без GPU
...

## Источники моделей
Для перевода требуются модели, которые могут быть получены 3 основными способами:

- обучить с помощью команды [marian](https://marian-nmt.github.io/docs/)
- обучить с помощью [обертки на Python для marian](https://huggingface.co/transformers/model_doc/marian.html)
- скачать с [репозитория huggingface](https://huggingface.co/Helsinki-NLP).
  Список доступных моделей получен с использованием скрипта в notebook.ipynb.

## Перевод
...

## Обучение
...

## Дообучение
...
