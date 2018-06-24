import pandas as pd

from gensim.models import word2vec
import logging
import jieba
import re
import csv

# remove the stopwords
# stop_path ='stop_words.txt'
# stpwrdlst = readfile(stop_path).splitlines()
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
train = pd.read_csv('JD.csv')
train_all=[]
for i in range(0, len(train['title'])):
    results=' '.join(train['title'])
    train_all.append(results.split())
model = word2vec.Word2Vec(train_all, size=100, window=10, sg=0)
model.save('product_model.bin')
model.wv.save_word2vec_format("product_model.txt", binary=False)


word_list=[]
cf = open("product_vec_train.txt", "a", encoding='utf-8')
words=readfile("product_model.txt").splitlines()
for i in range(1,len(words)):
    word_list.append(words[i].split()[0])

for i in range(0, len(train['title'])):
    temp = []
    cf.write(str(i+1)+' ')
    for word in train['title'][i].split():
        if word in word_list:
            if word not in temp:
                temp.append(word)
                result = str(model[word]).replace('\n', '')
                cf.write(result+' ')
    cf.write('\n')
cf.close()

def readfile(path):
    fp = open(path, "r", encoding='utf-8', errors='ignore')
    content = fp.read()
    fp.close()
    return content