import random
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


def Preprocessing():
    # data.drop_duplicates()      # 删除重复值
    # data.dropna()               # 删除缺失值
    for index in data.index:
        line = data.loc[index].values
        x.append(line[0:5])       # 获取原数据集中的属性

    print("--------数据集预处理-----------")
    for i in range(0,len(x)):
        print(i,x[i])
    return x


def indexNum(E):
    ret = 0
    for i in range(0, len(x)):
        if all(E == x[i]):
            return ret
        else:
            ret += 1


def Denary2Binary(n):               # 十进制转二进制
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n < 0:  raise ValueError # "must be a positive integer"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr

def int2string(i):
    a = '%d' % i
    return a

def string2int(s):
    i = int(s)
    return i


if __name__ == '__main__':

     #j = generateRan(i)
     #print(j)
     print("-------------start---------------")
     # ret = Preprocessing(0.5)
     y = Preprocessing()                # 对数据集进行预处理

     print("---------------转换成01字符串---------------")
     for i in range(0,len(y)):
        b = Denary2Binary(indexNum(y[i])).zfill(10)
        print(b)


     print("---------------对每一位上添加扰动噪声---------------")
     for i in range(0,len(y)):
         b = Denary2Binary(indexNum(y[i])).zfill(10)
         a = b[0:2]
         c = string2int(b[2:10])
         d = [0,0,0,0,0,0,0,0]
         j = 1
         while c != 0:
             d[-j] = c%10
             c = c//10
             j+=1
         for j in range(len(d)):
             d[j] = PerturbI(d[j],0.5)
         print(d)

