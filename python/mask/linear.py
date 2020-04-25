import numpy as np
from sklearn.linear_model import LinearRegression

def linear(train,pos):    
    y = []
    lr_x = []
    for i in range(len(train)):
        y.append(train[i][pos])
        lr_x.append(train[i][0:745])
    y = np.reshape(y,newshape=(i+1,1))

    lr = LinearRegression()
    lr.fit(lr_x,y)
    lastlist = np.argsort(lr.coef_[0],axis=0)
    gentic = lastlist.tolist()
    return gentic