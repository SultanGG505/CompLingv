path = "DataSet.Txt"  # Путь к файлу с датасетом

from nltk import sent_tokenize  # импортирование пакета для разделения текста на предложения
from nltk import word_tokenize  # импортирование пакета для разделения предложений на слова

file = open(path, "r", encoding="utf8")  # открытие файла с текстом датасета

text = file.readlines()  # чтение всех строк из файла с текстом датасета
d = 1  # переменная для нумерации предложений в тексте

# каждую строчку текста(с учётом того, что на одной строке документа может быть несколько предложений)
# разбиваем предложения, потом выводим каждое предложение, причём выведя предложение, сразу разбиваем его на слова
# и тоже выводим их
for el in text:
    sentences = sent_tokenize(el)
    for i in range(len(sentences)):
        print("Предложение номер " + " " + str(d) + ": " + str(sentences[i]))
        sent = sentences[i]
        d += 1
        words = word_tokenize(sent)
        print("Слова из этого предложения: ", sep="")
        print(words, sep=" ")
        print("\n")
