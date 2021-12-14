from sentence_splitter import SentenceSplitter, split_text_into_sentences
from sys import argv

text = ' '.join(argv[1:])
print("\n".join((split_text_into_sentences(text, language='en'))))

