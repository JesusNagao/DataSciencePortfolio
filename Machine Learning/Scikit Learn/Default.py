from os import sep
from numpy.core.fromnumeric import size, transpose
from numpy.core.numeric import empty_like
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data=pd.read_csv('Default.txt', sep="\t", header=0)

y=np.array([data['default']]).T
x=np.array([data['student'], data['balance'], data['income']]).T

for j in range(size(y)):
    for k in range(3):
        if(x[j,k] == "No"):
            x[j,k] = 0
        elif(x[j,k] == "Yes"):
            x[j,k] = 1

for j in range(size(y)):
    if(y[j] == "No"):
        y[j] = 0
    elif(y[j] == "Yes"):
        y[j] = 1

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

b = np.empty((size(y_train),size(y_train)))

b_trans = np.transpose(x_train)
x_train_trans = np.transpose(x_train)

iter = 1
a = 0.3
i=0



while i<iter:
    for j in range(size(y_train)-1):
        for k in range(3):
            print(j)
            mu = 1/(1+np.exp(-np.transpose(b[:,j])*x_train[k,j]))
            grad_b = np.dot(np.transpose(x_train),(mu-y_train))
            b[:,j+1] = b[:,j] - a*grad_b[j,:]
            #print(grad_b.shape)
    i += 1

print(b)