#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np


# In[9]:


def dec(l,M,V,point,center):
    
    #收集训练集
    train = [0 for x in range(V)]
    
    #停车点个数
    P = len(center)
    
    #平均停放上限
    vehicleLimit = round(V/P/0.75)
    
    #统计距离代价
    minDis = 0
    
    #统计密度代价
    variance = 0
    vehicleAvg = round(V/P)
    
    #统计各停放点停车数量
    stopNum = []
    for x in range(P):
        stopNum.append(0)
        
    for i in range(V):
        
        #可用标志位
        available = 0
        
        for j in range(P):
            #存放该车辆到当前停车点的距离
            disTemp = np.sqrt(np.sum(np.square(np.array(point[l[i]])-np.array(center[j]))))
            #初始化最近距离和停车点编号（不考虑竞争）
            if j == 0:
                minTemp = disTemp
                minNum = j
                
            #更新最近的距离和编号（不考虑竞争）
            if disTemp < minTemp:
                minTemp = disTemp
                minNum = j
                
            if stopNum[j] < vehicleLimit:#实际有停车位时
                if available == 0:
                    dis = disTemp
                    trueNum = j
                    available = 1
                if disTemp < dis:
                    dis = disTemp
                    trueNum = j
                    
        #判断是否停到了最近的停车位(机器学习编码)
        if trueNum == minNum:
            train[l[i]] = 1
        else:
            train[l[i]] = 0
                
        #计算距离代价和车辆停放情况        
        minDis = minDis + dis
        stopNum[trueNum] = stopNum[trueNum] + 1
    
    #计算密度代价
    for i in range(P):
        variance = variance + (stopNum[i] - vehicleAvg) ** 2
        
    l.append(minDis)
    l.append(variance)
    
    return l,train


# In[ ]:




