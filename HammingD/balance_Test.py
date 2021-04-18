#  引用自 https://blog.csdn.net/qq_41528502/article/details/108954544
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd
import graphviz
from sklearn import tree
data = pd.read_csv('balance-scale.data', header=None)

x_old = []  # 存放原数据集中的属性
y_old = []  # 存放原数据集中的标签
x_train = []  # 存放训练集的属性
y_train = []  # 存放训练集的标签
x_test = []  # 存放测试集的属性
y_test = []  # 存放测试集的标签
testSize = 0.5  # 测试数据所占总数据比重

'''数据预处理'''


def Preprocessing():
    data.drop_duplicates()  # 删除重复值
    data.dropna()  # 删除缺失值
    # x_old = []                    # 临时存储原属性值 用于合成扩增数据集中的属性值
    for index in data.index:
        line = data.loc[index].values
        x_old.append(line[1:5])  # 获取原数据集中的属性
        y_old.append(line[0])  # 获取原数据集中的标签



'''决策树方法'''

def DecisionTree(testSize):
    print('------------------------决策树方法------------------------')
    print('原数据集：')
    x_train, x_test, y_train, y_test = train_test_split(x_old, y_old, test_size=testSize)
    clf = DecisionTreeClassifier(criterion='gini',max_depth=5,max_features=4)
    clf.fit(x_train, y_train)
    #dot_data = tree.export_graphviz(clf, out_file=None)
    #graph = graphviz.Source(dot_data)
    #graph.render(r'C:\Users\BO\Desktop\balance')
    y_predict = clf.predict(x_test)
    print(clf.score(x_test, y_test))
    print(classification_report(y_test, y_predict))


'''随机森林方法'''

def RandomForest(testSize):
    print('------------------------随机森林方法------------------------')
    print('原数据集：')
    x_train, x_test, y_train, y_test = train_test_split(x_old, y_old, test_size=testSize)
    rfc = RandomForestClassifier()
    rfc.fit(x_train, y_train)
    y_predict = rfc.predict(x_test)
    print(rfc.score(x_test, y_test))
    print(classification_report(y_test, y_predict))


if __name__ == '__main__':
    Preprocessing()
    DecisionTree(testSize)
