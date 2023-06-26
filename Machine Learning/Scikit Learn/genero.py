from numpy.core.fromnumeric import size, transpose
from numpy.core.numeric import empty_like
import pandas as pd
import numpy as np

x=pd.read_csv('genero.txt', skiprows=1, usecols=[1]).to_numpy()
y=pd.read_csv('genero.txt', skiprows=1, usecols=[2]).to_numpy()

x_train=x[:round(x.size*0.8)]
x_pred=x[round(x.size*0.2):]

y_train=y[:round(y.size*0.8)]
y_pre=y[round(y.size*0.2):]

b = np.empty((size(x_train),size(y_train)))

b_trans = np.transpose(x_train)
x_train_trans = np.transpose(x_train)

iter = 1
a = 0.3
i=0

while i<iter:
    for j in range(size(x_train)-1):
        print(j)
        mu = 1/(1+np.exp(-np.transpose(b[:,j])*x_train[j]))
        grad_b = np.transpose(x_train)*(mu-y_train)
        b[:,j+1] = b[:,j] - a*grad_b[:,j]
    i += 1

print(b)
