import math
import numpy as np
import random
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size


class Vendedores:

    def __init__(self, n_ciudades, iteraciones, coordenadas):
        self.n_ciudades = n_ciudades
        self.it = iteraciones
        self.coor = coordenadas
        self.main()

        

    def dist(self, ciudad):
        d = math.sqrt(ciudad[0]**2+ciudad[1]**2)
        return d

    def cadenaMarkov(self, du, dv, u, v,T):

        if dv<du:
            u = v
        else:
            if np.random.randint(0,1)<math.exp(-(dv-du)/T):
                u=v

        return u

    def distBest(self, best, coor):

        d = 0

        
        for i in range(size(best)):
            
            d += self.dist(coor[int(best[i]),:])
        
        return d


    def vecino(self, lk):

        v = np.random.randint(0, self.n_ciudades)
        band = True

        while band:
            j=1
            for i in range(size(lk)):
                if v == lk[i]:
                    v = np.random.randint(0, self.n_ciudades)
                    j=0

            if j!=0:
                band = False


        return v

    def main(self):
        a = random.random()
        cont = 0
        d_best = 0

        while cont<self.it: 

            
            u = np.random.randint(0,self.n_ciudades)
            lk = np.zeros(self.n_ciudades)
            best_lk = np.zeros(self.n_ciudades)


            for i in range(size(lk)):
                lk[i] = -1
                best_lk[i] = -1

            lk[0] = u

            d=0
            T=0.1
            i = 0

            
            for l in range(self.n_ciudades):
                
                v = self.vecino(lk)
            
                du = self.dist(self.coor[u,:])
                dv = self.dist(self.coor[v,:])


                u = self.cadenaMarkov(du, dv, u, v, T)
                d += self.dist(self.coor[u,:])

                T = a*T

                lk[i] = u
                i+=1


            d_best = self.distBest(best_lk, self.coor)

            if d_best>0:
                if d_best>d:
                    best_lk = lk
            else:
                best_lk = lk
            

            cont+=1


        ax = plt.axes()

        for i in range(size(lk)-1):
            ax.arrow(self.coor[int(lk[i]),0], self.coor[int(lk[i]),1], self.coor[int(lk[i+1]),0]-self.coor[int(lk[i]),0], self.coor[int(lk[i+1]),1]-self.coor[int(lk[i]),1], head_width=0.3, head_length=0.2, fc='lightblue', ec='black')
        ax.arrow(self.coor[int(lk[self.n_ciudades-1]),0], self.coor[int(lk[self.n_ciudades-1]),1], self.coor[int(lk[0]),0]-self.coor[int(lk[self.n_ciudades-1]),0], self.coor[int(lk[0]),1]-self.coor[int(lk[self.n_ciudades-1]),1], head_width=0.3, head_length=0.2, fc='lightblue', ec='black')

        d = 0
        for i in range(self.n_ciudades-1):
            d = d + math.sqrt((coor[int(lk[i]),0]-coor[int(lk[i+1]),0])**2+(coor[int(lk[i]),1]-coor[int(lk[i+1]),1])**2)
        d = d + math.sqrt((coor[int(lk[0]),0]-coor[int(lk[self.n_ciudades-1]),0])**2+(coor[int(lk[0]),1]-coor[int(lk[self.n_ciudades-1]),1])**2)
        plt.scatter(self.coor[:,0], self.coor[:,1])
        plt.show()


n_ciudades = 90
x = [ 65, 38,	81,	54,	36,	94,	88,	55,	63,	59,	22,	31,	48,	24,	85,	20,	23,	18,	24,	44,	32,	92,	44,	19,	91,	98,	44,	12,	27,	41,	60,	27,	61,	71,	23,	13,	30,	33,	43,	51,	9,	27	,80,	4,	93,	73,	49,	58,	24,	46,	96,	55,	53,	24,	49,	63,	68,	40,	37,	99,	5,	89,	91,	80,	11,	27,	34,	68,	15,	72,	12,	66,	50,	78,	72,	90,	89,	34,	70,	21,	4,	75,	51,	49,	91,	61,	62,	86,	81,	58]
y = [19,	25,	89,	4,	50,	18,	98,	72,	51,	48,	7,	69,	5,	8,	53,	11,	82,	82,	73,	16,	66,	52,	97,	65,	80,	46,	44,	83,	9,	14,	18,	40,	83,	81,	7,	41,	53,	42,	66,	63,	30,	44,	3,	98,	18,	12,	38,	21,	49,	35,	95,	92,	6,	74,	28,	43,	55,	94,	42,	98,	31,	70,	67,	54,	70,	67,	19,	14,	100,	18,	4,	57,	88,	67,	20,	38,	47,	98,	16,	86,	65,	38,	20,	43,	49,	13,	59,	23,	39,	59]
#coor = np.random.randint(1,2)*np.random.random_sample(size=(n_ciudades, 2))*1
#print(x)
coor = np.column_stack((x, y))
iteraciones = 100000
k = 1 # vendedores

vend = [None] * k

for i in range(k):
    vend[i] = Vendedores(n_ciudades, iteraciones, coor)
