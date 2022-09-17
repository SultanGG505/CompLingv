path = "DataSet.Txt"

from nltk import download
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords

file = open(path, "r", encoding="utf8")
# download('stopwords')
#
# stop_words = set(stopwords.words('russian'))

text = file.readlines()
d = 0
for el in text:
    sentences = sent_tokenize(el)
    for i in range(len(sentences)):
        print("Предложение номер " + " " + str(d) + ": " + str(sentences[i]))
        sent = sentences[i]
        d += 1
        words = word_tokenize(sent)
        print("Слова из этого предложения: ", sep="")
        print(words,sep=" ")
        print("\n")
