#Greedy Best First Search


import numpy as np
import math
from copy import deepcopy

def distance(p1, p2, n):

    #Calculo de la distancia euclidiana entre el estado actual y el estado meta

    sum = 0

    for i in range(0, n-1):
        for j in range(0, n-1):
            
            sum = sum + (p1[i][j] - p2[i][j])**2

    return math.sqrt(sum)

def sort(c, p_final, n):

    #Bubble sort para ordenar el costo de las 

    for i in range(0, len(c)):

        c = list(c)

        for j in range(0, len(c)-i-1):
            if (distance(c[j], p_final, n) > distance(c[j+1], p_final, n)):
                #c[j], c[j+1] = c[j+1], c[j]
                temp = deepcopy(c[j])
                c[j] = deepcopy(c[j+1])
                c[j+1] = deepcopy(temp)

    return c

def is_seen(p, seen):

    #revision para evitar que se repitan estados.

    band = False
    for i in range(0, len(seen)):
        if (np.array_equal(p, seen[i].get_p())):
            band = True
    
    return band

class Node:

    #Clase nodo la cual tiene asignado un p el cual es el estado representado

    def __init__(self, p):
        self.p = p

    def genNeighbors(self):

        #funcion que genera los nodos vecinos del nodo actual

        if self.p[1][1] == 0:
            p1 = np.copy(self.p)
            p1[1][1] = self.p[0][1]
            p1[0][1] = 0

            p2 = np.copy(self.p)
            p2[1][1] = self.p[1][0]
            p2[1][0] = 0

            p3 = np.copy(self.p)
            p3[1][1] = self.p[1][2]
            p3[1][2] = 0

            p4 = np.copy(self.p)
            p4[1][1] = self.p[2][1]
            p4[2][1] = 0

            return p1, p2, p3, p4

        elif self.p[0][1] == 0:
            p1 = np.copy(self.p)
            p1[0][1] = self.p[0][0]
            p1[0][0] = 0

            p2 = np.copy(self.p)
            p2[0][1] = self.p[0][2]
            p2[0][2] = 0

            p3 = np.copy(self.p)
            p3[0][1] = self.p[1][1]
            p3[1][1] = 0

            return p1, p2, p3

        elif self.p[1][0] == 0:
            p1 = np.copy(self.p)
            p1[1][0] = self.p[0][0]
            p1[0][0] = 0

            p2 = np.copy(self.p)
            p2[1][0] = self.p[2][0]
            p2[2][0] = 0

            p3 = np.copy(self.p)
            p3[1][0] = self.p[1][1]
            p3[1][1] = 0

            return p1, p2, p3

        elif self.p[1][2] == 0:
            p1 = np.copy(self.p)
            p1[1][2] = self.p[0][2]
            p1[0][2] = 0

            p2 = np.copy(self.p)
            p2[1][2] = self.p[2][2]
            p2[2][2] = 0

            p3 = np.copy(self.p)
            p3[1][2] = self.p[1][1]
            p3[1][1] = 0

            return p1, p2, p3

        elif self.p[2][1] == 0:
            p1 = np.copy(self.p)
            p1[2][1] = self.p[2][2]
            p1[2][2] = 0

            p2 = np.copy(self.p)
            p2[2][1] = self.p[2][0]
            p2[2][0] = 0

            p3 = np.copy(self.p)
            p3[2][1] = self.p[1][1]
            p3[1][1] = 0

            return p1, p2, p3

        elif self.p[0][0] == 0:
            p1 = np.copy(self.p)
            p1[0][0] = self.p[0][1]
            p1[0][1] = 0

            p2 = np.copy(self.p)
            p2[0][0] = self.p[1][0]
            p2[1][0] = 0

            return p1, p2

        elif self.p[0][2] == 0:
            p1 = np.copy(self.p)
            p1[0][2] = self.p[0][1]
            p1[0][1] = 0

            p2 = np.copy(self.p)
            p2[0][2] = self.p[1][2]
            p2[1][2] = 0

            return p1, p2

        elif self.p[2][0] == 0:
            p1 = np.copy(self.p)
            p1[2][0] = self.p[2][1]
            p1[2][1] = 0

            p2 = np.copy(self.p)
            p2[2][0] = self.p[1][0]
            p2[1][0] = 0

            return p1, p2

        elif self.p[2][2] == 0:
            p1 = np.copy(self.p)
            p1[2][2] = self.p[1][2]
            p1[1][2] = 0

            p2 = np.copy(self.p)
            p2[2][2] = self.p[2][1]
            p2[2][1] = 0

            return p1, p2

    def get_p(self):

        #funcion para obtener el estado actual del puzzle

        return self.p

#Inicializamos variables

p = np.array([[3, 1 ,0] , [6 ,8, 5] , [7, 4, 2]])
p_final = np.array([[0, 1, 2] , [3, 4, 5] , [6, 7, 8]])
n = 3

#El arreglo queue nos sirve para saber cual es el siguiente vecino a visitar
#El arreglo seen nos sirve para evitar los estados repetidos
queue = []
queue.append(Node(p))
seen = []
seen.append(queue[0])
index = 0

#Loop principal, corre mientras el algoritmo no haya encontrado la solucion.
while ((not np.array_equal(queue[0].get_p(), p_final))):
    #generamos los nuevos vecinos y los acomodamos por distancia a la solucion original
    c = queue[0].genNeighbors()
    c = sort(c, p_final, n)
    
    #Agregamos los vecinos a la lista de espera y a los estados vistos
    for i in range(0, len(c)):
        if (not is_seen(c[i], seen)):
            queue.append(Node(c[i]))
            seen.append(Node(c[i]))

    #Si la solucion se encontro, se guarda
    if (np.array_equal(queue[0].get_p(), p_final)):
        sol = queue[0]
        print(queue[0].get_p())
    
    #Eliminamos de la lista de espera el estado actual
    del queue[0]
    index = index + 1

#print(sol.get_p())