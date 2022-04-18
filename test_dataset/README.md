# Целевые наборы данных

## Группы набора данных 
Каталог включает три группы набора данных:

* транзитивный набор данных:
```
.
├── test_dataset.xlsx  # сводные данные
├── input.ar  # предложения на арабском языке
├── input.en  # предложения на английском языке
└── input.ru  # предложения на русском языке
```

*  англо-русский разговорник в IT-сфере:
```
.
├── messages.html   # исходный файл фраз из канала (https://t.me/english_easily)
├── prog_vocab.xlsx # извлеченные фразы
├── corrected_vocab.xlsx  # откорректированные фразы (1038)
├── translated_vocab.xlsx # переведенные фразы
└── diff_translated_vocab.xlsx # фразы, отличные от эталона
```

* англо-русский разговорник обыденных фраз:
```
.
├── normal.xlsx  # сформированные фразы (2664)
├── translated_normal.xlsx  # переведенные фразы
└── diff_translated_normal.xlsx  # фразы, отличные от эталона
```

* англо-русский корпус из тестового набора данных, используемый для модели [Helsinki-NLP
/
opus-mt-ru-en](https://huggingface.co/Helsinki-NLP/opus-mt-ru-en)
```
.
├── test_en-ru_opus_1-src_2-tgt_3-translation.txt # исходный файл (5000)
└── test_opus_en-ru_dataset.xlsx # корпус en-ru
```

## Сценарии для работы с набором данных 

Файл
```programmer_vocabs.ipynb```
реализует задачи формирования целевых наборов данных.
