import numpy as np


if __name__ == '__main__':

    v1=np.array([1,1,0,1,0,1,0,0,1])
    v2=np.array([1,1,1,0,0,0,1,1,1])
    smstr=np.nonzero(v1-v2)
    print(smstr) # 不为0的元素的下标
    sm= np.shape(smstr[0])[0]
    print(sm)
    #输出
    #(array([0, 2, 3, 5, 6, 7]),)
    #6