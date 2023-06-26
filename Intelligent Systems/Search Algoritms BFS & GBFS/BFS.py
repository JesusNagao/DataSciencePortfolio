#Breadth-first search

import numpy as np

p_init = np.array([[3, 1 ,0] , [6 ,8, 5] , [7, 4, 2]])
p_final = np.array([[0, 1, 2] , [3, 4, 5] , [6, 7, 8]])

class Parent:
    def __init__(self, p):
        self.p = p
        self.visited = False

    def genChildren(self):
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
        return self.p

    def visit(self):
        self.visited = True

    def get_visited(self):
        return self.visited



def is_not_seen(c, seen):
    
    band = True

    for i in range(0, len(seen)):
        if (c == seen[i]).all():
            band = False
    
    return band

parent = []
parent.append(Parent(p_init))
index = 0

seen = [p_init]

print("Initial State:")
print(p_init)

while not np.array_equal(parent[index].get_p(), p_final):

    c = parent[index].genChildren()
    child = []

    for j in range(0, len(c)):
        if is_not_seen(c[j], seen):
            parent.append(Parent(c[j]))
            seen.append(c[j])

    index = index + 1

print(index)
print("Final State:")
print(parent[index].get_p())

