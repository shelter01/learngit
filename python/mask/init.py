import numpy as np
from eva import eva
#初始化操作，chro种群矩阵带适应度，ran打乱顺序
def init(pop,V,dis):
    chro = []
    ran = []
    train = []
    for i in range(V):
        ran.append(i)
    for i in range(pop):
        np.random.shuffle(ran)
        chro.append(ran[:])
        train.append(eva(chro[i],V,dis))
    return chro,train