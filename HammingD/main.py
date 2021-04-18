import random

import pandas as pd
import math

i =0.0
N = 5

data = pd.read_csv('balance-scale.data', header=None)
x = []  # 存放原数据集中的属性
y = []  # 存放原数据集中的标签


def generateRan():

    #count_list = [1,2,3,4,5]
    #a = random.choice(count_list)
    #print(a)
    n = random.random()
    return n

def PerturbI(i,e):
    p = (math.exp(e))/(4+math.exp(e))
    n = generateRan()
    z = [1,2,3,4,5]    #属性候选值

    z.remove(i)

    if n > p:
        return i
    else:
        z = random.choice(z)
        return z

def PerturbII(j,e):
    p = (math.exp(e)) / (4 + math.exp(e))
    n = generateRan()
    o = ['L', 'B', 'R']  # 类标签候选值
    o.remove(j)
    if n>p:
        return j
    else:
        o = random.choice(o)
        return o


def Preprocessing(e):
    # data.drop_duplicates()  # 删除重复值
    # data.dropna()  # 删除缺失值

    a_ret = []
    for index in data.index:
        line = data.loc[index].values
        x.append(line[1:5])  # 获取原数据集中的属性
        y.append(line[0])  # 获取原数据集中的标签

    print("--------原始数据集-----------")
    for i in range(0,len(x)):
        print(i+1,x[i],y[i])
    print("------扰动之后的数据集------")
    for i in range(0, len(x)):
        for j in range(0,len(x[0])):
            x[i][j] = PerturbI(x[i][j],e)
    for i in range(0,len(y)):
        y[i] = PerturbII(y[i],e)
    for i in range(0,len(x)):
        a = []
        for j in range(0,5):
            if j <4:
                a.append(x[i][j])
            elif j == 4:
                a.append(y[i])
        a_ret.append(a)
    return a_ret



if __name__ == '__main__':

     #j = generateRan(i)
     #print(j)
     print("-------------start---------------")
     ret = Preprocessing(0.5)

     print(ret)
