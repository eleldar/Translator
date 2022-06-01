from langdetect import detect


def sent_detection(sent, direct):
    '''Language ID adaptred for fasttext model'''
    lang_id =  detect(sent)
    src_id, tgt_id = direct.split('-')
    black_list = [tgt_id, 'uk', 'bg', 'cs', 'mk']
    return (lang_id == src_id or lang_id not in black_list)


if __name__ == '__main__':
    text = 'hello world!'    
    print(sent_detection(text, 'en-ru'))
