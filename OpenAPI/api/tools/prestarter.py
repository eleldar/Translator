import os
from pathlib import Path
import codecs

drive, path_and_file = os.path.splitdrive(Path(__file__).absolute())
path, _ = os.path.split(path_and_file)
curdir = os.path.join(drive, path)
files_path = os.path.join(curdir, 'prestart_examples')

def examples(direct):
    language_id = direct.split('-')[0]
    file = os.path.join(files_path, f'input.{language_id}')
    try:
        with codecs.open(file, "r", "utf_8_sig") as f:
            text = f.readlines()
    except FileNotFoundError:
        text = []
    return text

if __name__ == '__main__':
    print(examples('en-ru'))
