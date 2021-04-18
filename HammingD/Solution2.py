import pandas as pd




data = pd.read_csv('data1.data', header=None)
x = []


# 数据预处理
def Preprocessing():
    for index in data.index:
        line = data.loc[index].values
        x.append(line[0:625])       # 获取原数据集中的属性

    print("--------数据集预处理-----------")
    for i in range(0,len(x)):
        print(i, x[i])
    return x


if __name__ == '__main__':
    x = Preprocessing()
