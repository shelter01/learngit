import random
from eva import eva

def ope(chro,M,V,dis,train):
    for i in range(len(chro)):
        child = chro[i][0:V]
        pos = round(random.random()*(round(V/2-1)))
        temp = child[0:pos]
        child[0:pos] = child[V-pos:V]
        child[V-pos:V] = temp
        train.append(eva(child,V,dis))
        chro.append(child)