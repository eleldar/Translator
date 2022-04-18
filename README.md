# Переводчик

Проект по использовани нейронного машинного перевода (neural machine translation, NMT)

## Цель проекта
Разработка моделей, адаптированных для перевода тематических предметных областей без потери качества исходных моделей.


## Инструменты

В открытом доступе существует значительное число ресурсов с готовыми решениями нейронного машинного перевода. Наиболее популярными решениями являются:
Решение | Язык | Фреймворк
---|---|---
TENSOR2TENSOR    |Python     |TensorFlow
FAIRSEQ          |Python     |PyTorch
NMT	         |Python     |TensorFlow
OPENNMT          |Python/C++ |PyTorch/TensorFlow
SOCKEYE          |Python     |MXNet
NEMATUS	         |Python     |Tensorflow
MARIAN	         |C++	     |–   
THUMT	         |Python     |PyTorch/TensorFlow
NMT-KERAS	 |Python     |Keras
NEURAL MONKEY	 |Python     |TensorFlow
TRANSFORMERS HUB |Python     |PyTorch/TensorFlow/JAX

## Структура

```
.
├── OpenAPI
│   ├── __pycache__
│   ├── api
│   │   ├── __pycache__
│   │   └── tools
│   │       └── __pycache__
│   ├── documented_endpoints
│   │   ├── __pycache__
│   │   └── translations
│   │       ├── __pycache__
│   │       └── api -> ../../api
│   ├── models
│   └── venv
├── articles
├── data
│   └── MNIST
│       └── raw
├── examples
│   ├── DeepPavlov_translation
│   │   ├── marianmt-tatoeba-enru
│   │   └── marianmt-tatoeba-ruen
│   ├── Opus-MT_translation
│   ├── create_datasets
│   ├── marian-nmt
│   │   ├── ar_en
│   │   │   ├── afa
│   │   │   │   ├── marian-dev -> /home/eldar/marian-dev
│   │   │   │   ├── model
│   │   │   │   └── mosesdecoder
│   │   │   │       └── scripts
│   │   │   │           ├── generic
│   │   │   │           ├── recaser
│   │   │   │           ├── share
│   │   │   │           │   └── nonbreaking_prefixes
│   │   │   │           ├── tokenizer
│   │   │   │           └── training
│   │   │   └── sem
│   │   │       ├── model
│   │   │       ├── mosesdecoder
│   │   │       │   └── scripts
│   │   │       │       ├── generic
│   │   │       │       ├── recaser
│   │   │       │       ├── share
│   │   │       │       │   └── nonbreaking_prefixes
│   │   │       │       ├── tokenizer
│   │   │       │       └── training
│   │   │       └── tools -> /home/eldar/
│   │   ├── ar_ru
│   │   │   ├── model
│   │   │   ├── mosesdecoder
│   │   │   │   └── scripts
│   │   │   │       ├── generic
│   │   │   │       ├── recaser
│   │   │   │       ├── share
│   │   │   │       │   └── nonbreaking_prefixes
│   │   │   │       ├── tokenizer
│   │   │   │       └── training
│   │   │   └── tools -> /home/eldar/
│   │   ├── en_ar
│   │   │   ├── model
│   │   │   ├── mosesdecoder
│   │   │   │   └── scripts
│   │   │   │       ├── generic
│   │   │   │       ├── recaser
│   │   │   │       ├── share
│   │   │   │       │   └── nonbreaking_prefixes
│   │   │   │       ├── tokenizer
│   │   │   │       └── training
│   │   │   └── tools -> /home/eldar/
│   │   ├── en_ru
│   │   │   ├── marian-dev -> /home/eldar/marian-dev
│   │   │   ├── model
│   │   │   └── mosesdecoder
│   │   │       └── scripts
│   │   │           ├── generic
│   │   │           ├── recaser
│   │   │           ├── share
│   │   │           │   └── nonbreaking_prefixes
│   │   │           ├── tokenizer
│   │   │           └── training
│   │   ├── ru_ar
│   │   │   ├── model
│   │   │   ├── mosesdecoder
│   │   │   │   └── scripts
│   │   │   │       ├── generic
│   │   │   │       ├── recaser
│   │   │   │       ├── share
│   │   │   │       │   └── nonbreaking_prefixes
│   │   │   │       ├── tokenizer
│   │   │   │       └── training
│   │   │   └── tools -> /home/eldar/
│   │   └── ru_en
│   │       ├── model
│   │       ├── mosesdecoder
│   │       │   └── scripts
│   │       │       ├── generic
│   │       │       ├── recaser
│   │       │       ├── share
│   │       │       │   └── nonbreaking_prefixes
│   │       │       ├── tokenizer
│   │       │       └── training
│   │       └── tools -> /home/eldar/
│   ├── simple_translation
│   │   ├── data
│   │   └── score
│   ├── train
│   │   ├── Maverick_2.0_Translation_layer
│   │   ├── content
│   │   └── lalita-mt-zhth
│   │       ├── OpenSubtitles SentencePiece Model
│   │       ├── data
│   │       │   ├── OpenSubtitles
│   │       │   └── fairseq_tutorial
│   │       │       ├── binarized
│   │       │       ├── cleaned
│   │       │       ├── predictions
│   │       │       └── tokenized
│   │       ├── models
│   │       │   └── spm
│   │       ├── notebooks
│   │       │   └── marian-mt-zh_cn-th
│   │       └── scripts
│   ├── translation_with_fine_tune_model
│   │   └── first-fine-tuning-model
│   └── web_translation
│       └── venv
├── lightning_logs
│   ├── version_0
│   │   └── checkpoints
│   └── version_1
│       └── checkpoints
├── reports
│   ├── pretrained_model_test
│   └── repl_using
└── test_dataset
    └── flores101_dataset

2489 directories
```

