import os
from pathlib import Path
import codecs

# при импортировании адрес меняется на адрес пакета, поэтому директория вычисляемая
drive, path_and_file = os.path.splitdrive(Path(__file__).absolute())
path, _ = os.path.split(path_and_file)
curdir = os.path.join(drive, path)


def read_commands(direct):
    '''аргументы для замены исходных строк на целевые'''
    file = os.path.join(curdir, 'replace_commands', f'replace.{direct}')
    with codecs.open(file, 'r', 'utf_8_sig') as f:
        lines = f.readlines()
        commands = set(tuple(i.strip().split('/')[1:3]) for i in lines if '#' not in i)
    return commands


def get_commands(directs): 
    '''словарь команд для предобработки на основе 
    файла с расширением направления перевода и directs'''
    files = os.path.join(curdir, 'replace_commands')
    commands = {cp: read_commands(cp) for cp in directs if os.path.exists(os.path.join(files, f'replace.{cp}'))}
    return commands


def text_preprocess(text):
    '''предобработка всего текста'''
    text = text.replace('&#xD;&#xA;', ' ')
    text = text.replace('\n', ' ')
    return text


def sent_preprocess(commands, text):
    '''предобработка предложения'''
    for command in commands:
        text = text.replace(command[0], command[1])
        text = text.replace('\\', '')
    return text


if __name__ == '__main__':
    directs = [ # пример списка направлений
       'en-ru',
       'ar-en'
    ]
    print(get_commands(directs))
