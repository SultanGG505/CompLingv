path = "DataSet.Txt"  # Путь к файлу с датасетом

from nltk import sent_tokenize  # импортирование пакета для разделения текста на предложения
from nltk import word_tokenize  # импортирование пакета для разделения предложений на слова
from nltk.corpus import stopwords

file = open(path, "r", encoding="utf8")  # открытие файла с текстом датасета
text = file.readlines()  # чтение всех строк из файла с текстом датасета
d = 1  # переменная для нумерации предложений в тексте

import numpy as np

sents = []
for el in text:
    sentences = sent_tokenize(el)
    for i in range(len(sentences)):
        print("Предложение номер " + " " + str(d) + ": " + str(sentences[i]))
        sent = sentences[i]
        sents.append(sent)
        d += 1

print("Всего предложений в тексте: " + str(len(sents)))


nums = sents
def tfidf(word):
    tf = []
    count_n = 0
    for sentence in nums:
        # calculate TF
        t_count = len([x for x in sentence if word in sentence])
        tf.append(t_count / len(sentence))
        # count number of docs for IDF
        count_n += 1 if word in sentence else 0
    try:
        idf = np.log10(len(nums) / count_n)
        return [round(_tf * idf, 2) for _tf in tf]
    except Exception as err:
        print("В данной системе нет ответа на данный запрос")
        quit()



nums = tfidf(input("Введите запрос"))

for d in range(len(nums)):
    print(d + 1, nums[d])

max_res = max(nums)
ind = []

for d in range(len(nums)):
    if max_res == nums[d]:
        ind.append(d)

print("Наиболее похожие предложения по запросу: ")

for el in ind:
    print(sents[el])



# a = tfidf('поисковыми системами')
# print(f"TF-IDF a: {a}\nTF-IDF b: {a}\nTF-IDF c: {a}")
#
# vocab = set(a+b+c)

# print(vocab)
#
#
# # initialize vectors
# vec_a = []
# vec_b = []
# vec_c = []
#
# for word in vocab:
#     tfidf_a, tfidf_b, tfidf_c = tfidf(word)
#     vec_a.append(tfidf_a)
#     vec_b.append(tfidf_b)
#     vec_c.append(tfidf_c)
#
# print(vec_a)
# print(vec_b)
# print(vec_c)
