path = "DataSet.Txt"  # Путь к файлу с датасетом

from nltk import sent_tokenize  # импортирование пакета для разделения текста на предложения
from nltk import word_tokenize  # импортирование пакета для разделения предложений на слова

from pymorphy2 import MorphAnalyzer  # импортирование пакета для морфологического разбора слова

file = open(path, "r", encoding="utf8")  # открытие файла с текстом датасета

text = file.readlines()  # чтение всех строк из файла с текстом датасета
words = []  # массив слов

# все слова в датасете добавляем в переменную words
for el in text:
    sentences = sent_tokenize(el)
    for i in range(len(sentences)):
        sent = sentences[i]
        words += word_tokenize(sent)

morph = MorphAnalyzer()  # инициализируем MorphAnalyzer()

# для первых ста слов в датасете выводим их морфологический разбор

for i in range(100):
    print(str(morph.parse(words[i])) + "\n")
