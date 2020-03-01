def rep(chro,M,V,pop):
    comp = []
    res = []
    comp_rank = chro[pop-1][747]
    for i in range(len(chro)):
        if(chro[i][747]<comp_rank):
            res.append(chro[i])
        if(chro[i][747]==comp_rank):
            comp.append(chro[i])
    
    comp = sorted(comp, key=lambda s: s[748], reverse = True)
    flag = 0
    while(len(res)!=pop):
        res.append(comp[flag])
        flag = flag+1
    return res