import os
from pathlib import Path
import codecs

# при импортировании адрес меняется на адрес пакета, поэтому директория вычисляемая
drive, path_and_file = os.path.splitdrive(Path(__file__).absolute())
path, file = os.path.split(path_and_file)
curdir = os.path.join(path)

def read_commands(direct):
    '''аргументы для замены исходных строк на целевые'''
    file = f'{curdir}/replace.{direct}'
    with codecs.open(file, 'r', 'utf_8_sig') as f:
        lines = f.readlines()
        commands = set(tuple(i.strip().split('/')[1:3]) for i in lines if '#' not in i)
    return commands


def get_commands(directs): 
    '''словарь команд для предобработки на основе 
    файла с расширением направления перевода и directs'''
    commands = {cp: read_commands(cp) for cp in directs if os.path.exists(f'{curdir}/replace.{cp}')}
    return commands


def preprocess_text(commands, text):
    '''предобработка входного текста'''
    for command in commands:
        text = text.replace(command[0], command[1])
        text = text.replace('\\', '')
    return text


# пример словаря с моделями; в реальности не используется
directs = {
   'en-ru',
   'ar-en'
}

if __name__ == '__main__':
    print(get_commands(directs))
