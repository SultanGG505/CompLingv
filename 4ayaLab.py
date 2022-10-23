path = "DataSet.Txt"  # Путь к файлу с датасетом
from nltk import sent_tokenize  # импортирование пакета для разделения текста на предложения
import pymorphy2 as pm
from nltk import word_tokenize
import random
file = open(path, "r", encoding="utf8")  # открытие файла с текстом датасета
text = file.readlines()  # чтение всех строк из файла с текстом датасета
d = 1  # переменная для нумерации предложений в тексте
def freq_semantic(fragment_1, fragment_2):
    m = pm.MorphAnalyzer()
    words_1 = set([m.parse(word)[0].normal_form for word in
                   word_tokenize(fragment_1)])
    words_2 = set([m.parse(word)[0].normal_form for word in
                   word_tokenize(fragment_2)])
    return len(words_1 & words_2) / len(words_1)
mylist = []
for el in text:
    sentences = sent_tokenize(el)
    for i in range(len(sentences)):
        print("Предложение номер " + " " + str(d) + ": " + str(sentences[i]))
        sent = sentences[i]
        mylist.append(sent)
        d += 1
a = random.choice(mylist)
b = random.choice(mylist)
print("Первый фрагмент:", a, "\n", "Второй фрагмент:", b)
print(freq_semantic(a, b))
