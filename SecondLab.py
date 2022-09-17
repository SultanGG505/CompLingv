path = "DataSet.Txt"

from nltk import download
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords

from pymorphy2 import MorphAnalyzer

file = open(path, "r", encoding="utf8")

text = file.readlines()
words = []
for el in text:
    sentences = sent_tokenize(el)
    for i in range(len(sentences)):
        sent = sentences[i]
        words += word_tokenize(sent)

morph = MorphAnalyzer()

for i in range(100):
    print(str(morph.parse(words[i])[0]) + "\n")
