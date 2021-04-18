import random

import numpy as np
import pandas as pd
import math

# 扰动数据之不能恢复，拟解决方案是在扰动数据之前加入bloom过滤器等。
data = pd.read_csv('balance-scale.data', header=None)
x = []                 # 存放数据集
y = []                 # 训练用的数据集
def generateRan():                     # 生成随机数
    n = random.random()
    return n

def PerturbI(i,e):                     # 扰动
    e = e/8                            # 将隐私预算平均分配到8位上
    p = (math.exp(e))/(1+math.exp(e))  # w-RR 对二维数据进行扰动的概率为p
    n = generateRan()                  # 生成随机数

    if n > p:
        return i
    else:
        # z = random.choice(z)
        return 1-i


def Preprocessing():              # 数据集预处理
    # data.drop_duplicates()      # 删除重复值
    # data.dropna()               # 删除缺失值
    for index in data.index:
        line = data.loc[index].values
        x.append(line[0:5])       # 获取原数据集中的属性

    print("--------数据集预处理-----------")
    for i in range(0,len(x)):
        print(i+1,x[i])
    return x


def indexNum(E):
    ret = 0
    for i in range(0, len(x)):
        if all(E == x[i]):
            return ret
        else:
            ret += 1

def toString(E):
    a = np.arange(625)
    a = [int(b == -1) for b in a]
    a[indexNum(E)] = 1
    string = ",".join(map(str, a))
    return string


if __name__ == '__main__':

     #j = generateRan(i)
     #print(j)
     print("-------------start---------------")
     # ret = Preprocessing(0.5)
     y = Preprocessing()                # 对数据集进行预处理

     #a为01字符串


     print("->将数据集转换为0，1字符串，对应位为1保存为data1.data")
     f = open('data1.data', 'w')           #data1为处理好的字符串数据集
     for i in range(625):
         string = toString(y[i])
         f.write(string+'\n')
     f.close()



