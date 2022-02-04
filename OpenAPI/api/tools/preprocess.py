import os.path
import os
import codecs

# при импортировании адрес меняется на адрес пакета, поэтому добавляем эту диркторию
curdir = os.path.abspath(os.curdir) + '/api/tools'

def read_commands(direct):
    '''аргументы для замены исходных строк на целевые'''
    file = f'{curdir}/replace.{direct}'
    with codecs.open(file, 'r', 'utf_8_sig') as f:
        lines = f.readlines()
        commands = set(tuple(i.strip().split('/')[1:3]) for i in lines if '#' not in i)
    return commands


def get_commands(checkpoints): 
    '''словарь команд для предобработки на основе 
    файла с расширением направления перевода и checkpoints'''
    commands = {cp: read_commands(cp) for cp in checkpoints if os.path.exists(f'{curdir}/replace.{cp}')}
    return commands


def preprocess_text(commands, text):
    '''предобработка входного текста'''
    for command in commands:
        text = text.replace(command[0], command[1])
        text = text.replace('\\', '')
    return text


# пример словаря с моделями; в реальности не используется
checkpoints = {
   'en-ru': 'Helsinki-NLP/opus-mt-en-ru',
   'ar-en': 'Helsinki-NLP/opus-mt-ar-en',
}

if __name__ == '__main__':
    curdir = os.path.abspath(os.curdir)  
    print(get_commands(checkpoints))
