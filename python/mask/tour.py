import random

def tour(chro,pour_size,tour_size):
    pop = len(chro)
    V = (len(chro[0]))
    rank = V-2
    dis = V-1
    candi = [0,0]
    c_rank = [0,0]
    c_dis = [0,0]
    res = []
    for i in range(pour_size):
        for j in range(tour_size):
            candi[j] = round((pop-1)*random.random())
            if(candi[j]==0):
                candi[j]=1
            if(j>0):
                while(candi[j]==candi[j-1]):
                    candi[j] = round(pop*random.random())
                    if(candi[j]==0):
                        candi[j]=1
        for j in range(tour_size):
            c_rank[j] = chro[candi[j]][rank]
            c_dis[j] = chro[candi[j]][dis]
        min_candi = c_rank.index(min(c_rank))
        if(c_rank[0]==c_rank[1]):
            max_candi = c_dis.index(max(c_dis))
            res.append(chro[candi[max_candi]])
        else:
            res.append(chro[candi[min_candi]])
    return res