#!/bin/python3
import subprocess
import os

source = 'input.ar'
target = 'output.en'
with open(source, encoding='utf-8') as f:
    file = f.readlines()
if os.path.exists(target):
    os.remove(target)
for sent in [i.strip() for i in file]:
    command = f'echo "{sent}" | ./translate.sh >> {target}'
    os.system(command)
