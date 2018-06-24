import pandas as pd

from gensim.models import word2vec
import logging
import jieba
import re
import csv
def readfile(path):
    fp = open(path, "r", encoding='utf-8', errors='ignore')
    content = fp.read()
    fp.close()
    return content

def keyword2vec(keyword):
    print(keyword)
    new_model = word2vec.Word2Vec.load('./django_web/selectModel/product_model.bin')
    cf = open("./django_web/selectModel/keyword_vec.txt", "w", encoding='utf-8')
    word_list = []
    words = readfile("./django_web/selectModel/product_model.txt").splitlines()
    for i in range(1, len(words)):
        word_list.append(words[i].split()[0])

    for i in range(0, len(keyword)):
        temp = []
        cf.write(str(i + 1) + ' ')
        sentence = "".join(keyword[i])
        for word in sentence.split():
            if word in word_list:
                if word not in temp:
                    temp.append(word)
                    result = str(new_model[word]).replace('\n', '')
                    cf.write(result + ' ')
        cf.write('\n')
    cf.close()


