import numpy as np
from hv import HyperVolume

def score(chro):
    front = []
    for i in range(len(chro)):
        if(chro[i][747]==1):
            front.append(chro[i][745:747])
    #数组去重
    arr = np.array(front)
    front = np.array(list(set([tuple(t) for t in arr]))).tolist()
    #评分
    referencePoint = [700000, 1000]
    hyperVolume = HyperVolume(referencePoint)
    result = hyperVolume.compute(front)
    return result