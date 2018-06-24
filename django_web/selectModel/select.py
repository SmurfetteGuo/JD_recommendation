import numpy


def sim(w1, w2):
    """
    calculate the cosine of two vectors
    :param w1:
    :param w2:
    :return:
    """
    w1 = numpy.array(w1, dtype=float)
    w2 = numpy.array(w2, dtype=float)
    lm = numpy.sqrt(w1.dot(w1))
    ln = numpy.sqrt(w2.dot(w2))
    return w1.dot(w2) / (lm * ln)  # cos value


def getResult(S, T):
    """
    the similarity of the word bag T->S
    :param S:
    :param T:
    :return:
    """
    count = 0
    sum1 = 0
    for t in T:
        max1 = 0
        for s in S:
            temp = sim(t, s)
            if temp > max1:
                max1 = temp
        if max1 == 0:
            continue
        else:
            count = count + 1
            sum1 = sum1 + max1
    if count != 0:
        return max1 / count
    else:
        return 0


def main(train, test):
    result = []
    max1 = 0
    index = 0
    result_dic={}
    for i in range(len(train)):
        newTrain = train[i][1:]
        newTest = test[0][1:]
        temp = getResult(newTrain, newTest)
        result_dic[i]=temp
    result_dic = sorted(result_dic.items(), key=lambda d: d[1], reverse=True)
    # result.append(train[index][0])
    # sum1 = 0
    for i in range(0,24):
        result.append(result_dic[i][0])
    return result
        # if test[i][0] == result[i]:
        #     sum1 = sum1 + 1

    # print(sum1 / len(result))


def chu():
    list2 = [line.strip() for line in open("./django_web/selectModel/product_vec_train.txt", encoding='UTF-8')]
    list1 = [line.strip() for line in open("./django_web/selectModel/keyword_vec.txt", encoding='UTF-8')]
    # list1.append(keywords.split())
    newList2 = []
    newList1 = []
    for line in list2:
        newTemp = []
        newline = line.replace(']', '')
        list3 = newline.split('[')
        for i in range(len(list3)):
            if i == 0:
                newTemp.append(list3[i])
            else:
                newTemp.append(list3[i].split())
        newList2.append(newTemp)

    for line in list1:
        newTemp = []
        newline = line.replace(']', '')
        list3 = newline.split('[')
        for i in range(len(list3)):
            if i == 0:
                newTemp.append(list3[i])
            else:
                newTemp.append(list3[i].split())
        newList1.append(newTemp)

    return main(newList2, newList1)
