#目标函数求职，输入chro，维度，距离矩阵，返回一条训练集[3,1,2,4,222.22,2.2]，[0,1,1,0]
import numpy as np

def eva(chro,V,dis):
    P = len(dis[0])
    parkMax = round(V/P/0.9)
    parkAvg = V/P
    park = np.zeros(P).tolist()
    train = np.zeros(V).tolist()
    disSum = 0
    #遍历个体每个基因
    for i in range(V):
        #到停放区域距离的排序顺序索引（从小到大）
        index = np.argsort(dis[chro[i]])
        #遍历所有停放点（距离从小到大）
        for j in range(len(index)):
            #判断是否停满
            if(park[index[j]]<parkMax):
                park[index[j]] = park[index[j]]+1
                disSum = disSum+dis[chro[i]][index[j]]
                #判断是否停到最优（训练集）
                if(j==0):
                    train[chro[i]] = 1
                else:
                    train[chro[i]] = 0
                break
    #距离代价
    chro.append(disSum)
    
    sumAvg = 0
    for i in range(P):
        sumAvg = sumAvg+(park[i]-parkAvg)*(park[i]-parkAvg)
    #密度代价
    chro.append(sumAvg)
    
    train.append(disSum+sumAvg)
    train.append(disSum)
    train.append(sumAvg)
    return train