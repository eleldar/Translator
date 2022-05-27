# Программный интерфейс переводчика

## Структура файлов
```
.
├── api
│   ├── __init__.py
│   ├── tools
│   │   ├── preprocess.py
│   │   ├── replace.ar-en
│   │   ├── replace.ar-ru
│   │   ├── replace.en-ar
│   │   ├── replace.en-ru
│   │   ├── replace.ru-ar
│   │   └── replace.ru-en
│   └── translations.py
├── documented_endpoints
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-38.pyc
│   └── translations
│       ├── __init__.py
│       ├── __pycache__
│       │   └── __init__.cpython-38.pyc
│       └── api -> ../../api
├── main.py
└── requirements.txt
```
В директории api располагается программный код для обработки входного текста, 
а в директории documented_endpoints реализовано документирование специализации по стандарту OpenAPI.
Файл main.py можно запускать в режиме разработки через переменные среды:
```
flask runexport FLASK_APP=main.py
export FLASK_ENV=development
flask run
```
Виртуальную среду обязательно следует настраивать через requirements.txt,
т.к. имеются несовместимости среди текущих версий библиотек.
При наличии в системе GPU следует строку ```torch==1.10.1``` заменить на ```torch==1.10.1+cu113```.

