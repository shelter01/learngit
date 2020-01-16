#!/usr/bin/env python
# coding: utf-8

# In[8]:


import decoding_ga
import random
def ini(pop,M,V,point,center):
    
    chromosome = []
    train = []
    
    for i in range(pop):
        l = list(range(V))
        random.shuffle(l)
        #解码
        ch,tr = decoding_ga.dec(l,M,V,point,center)
        chromosome.append(ch)
        train.append(tr)
        
    return chromosome,train


# In[ ]:




