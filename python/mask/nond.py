import numpy as np

def nond(chro,M,V):
    #indi[0]是被支配数量，indi[1]是支配个体集合
    indi = []
    front = []
    front.append(1)
    front.append([])
    for i in range(len(chro)):
        indi.append([])
        indi[i].append(0)
        indi[i].append([])
        for j in range(len(chro)):
            dom_less = 0
            dom_equal = 0
            dom_more = 0
            for k in range(M):
                if(chro[i][V+k]<chro[j][V+k]):
                    dom_less = dom_less+1
                elif(chro[i][V+k]==chro[j][V+k]):
                    dom_equal = dom_equal+1
                else:
                    dom_more = dom_more+1
            if(dom_less==0 and dom_equal!=M):
                indi[i][0] = indi[i][0]+1
            elif(dom_more==0 and dom_equal!=M):
                indi[i][1].append(j)
        if(indi[i][0]==0):
            if(len(chro[i])==V+M):
                chro[i].append(1)
            chro[i][V+M] = 1
            front[1].append(i)
    
    while(front[1]):
        q = []
        #从支配为1的个体循环
        for i in range(len(front[1])):
            if(indi[front[1][i]][1]):
                #循环支配集合中的支配个体
                for j in range(len(indi[front[1][i]][1])):
                    indi[indi[front[1][i]][1][j]][0] = indi[indi[front[1][i]][1][j]][0]-1
                    if(indi[indi[front[1][i]][1][j]][0]==0):
                        if(len(chro[indi[front[1][i]][1][j]])==V+M):
                            chro[indi[front[1][i]][1][j]].append(front[0]+1)
                        chro[indi[front[1][i]][1][j]][V+M] = front[0]+1
                        q.append(indi[front[1][i]][1][j])
        front[0] = front[0]+1
        front[1] = q
    #按某一列排序
    print(1)
    chro = sorted(chro, key=lambda s: s[V+2])
    
    z = []
    #遍历pareto等级
    for i in range(chro[len(chro)-1][V+2]):
        dis = 0
        y = []
        #存同一层目标函数合集
        obj = [[],[]]
        #y[i]存同一等级的个体
        for j in range(len(chro)):
            if(chro[j][V+2]==i+1):
                y.append(chro[j])
                obj[0].append(chro[j][V])
                obj[1].append(chro[j][V+1])
        for k in range(M):
            index = np.argsort(obj[k])
            cow = sorted(y, key=lambda s: s[V+k])
            f_max = cow[len(cow)-1][V+k]
            f_min = cow[0][V+k]
            if(len(y[index[len(index)-1]])==V+M+k+1):
                y[index[len(index)-1]].append(float("-inf"))
            y[index[len(index)-1]][V+M+k+1] = float("-inf")
            if(len(y[index[0]])==V+M+k+1):
                y[index[0]].append(float("-inf"))
            y[index[0]][V+M+k+1] = float("-inf")
            for x in range(len(cow)-2):
                next_obj = cow[x+2][V+k]
                pre_obj = cow[x][V+k]
                if(f_max-f_min==0):
                    if(len(y[index[x+1]])==V+M+k+1):
                        y[index[x+1]].append(float("-inf"))
                    y[index[x+1]][V+M+k+1] = float("-inf")
                else:
                    if(len(y[index[x+1]])==V+M+k+1):
                        y[index[x+1]].append((next_obj-pre_obj)/(f_max-f_min))
                    y[index[x+1]][V+M+k+1] = (next_obj-pre_obj)/(f_max-f_min)
        
        for x in range(len(y)):
            y[x][M+V+1] = y[x][M+V+1]+y[x][M+V+2]
            z.append(y[x][0:len(y[0])-1])
    return z