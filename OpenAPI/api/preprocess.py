def replace_strings(direct):
    '''аргументы для замены исходных строк на целевые'''
    file = f'replace.{direct}'
    with open(file) as f:
        lines = f.readlines()
        commands = set(tuple(i.strip().split('/')[1:3]) for i in lines)
    return commands


def replaced_text(commands, text):
    '''предобработка входного текста'''
    for command in commands:
        text = text.replace(command[0], command[1])
        text = text.replace('\\', '')
    return text
