 -*- coding: utf-8 -*-
"""
Philosophers Stone
October 2018
@author: Nathalie
"""

    
T = [[3, 1, 7, 4, 2],
     [2, 1, 3, 1, 1],
     [1, 2, 2, 1, 8],
     [2, 2, 1, 5, 3],
     [2, 1, 4, 4, 4],
     [5, 2, 7, 5, 1]]
     

from algopy import matrix
from algopy import timing

def posMax(L):
    pos = 0
    for i in range(1, len(L)):
        if L[i] > L[pos]:
            pos = i
    return pos

#----------------- Greedy Algorith (algorithme glouton) ----------------------

@timing.timing
def HarryPotterGreedy(T):
    col = len(T[0])
    j = posMax(T[0])
    s = T[0][j]
    way = [j]
    for i in range(1, len(T)):
        j2 = j
        if j > 0 and T[i][j-1] > T[i][j2]:
            j2 = j - 1
        if j < col-1 and T[i][j+1] > T[i][j2]:
            j2 = j + 1
        j = j2
        way.append(j)
        s += T[i][j]
    return (s, way)



#----------------- Dynamic Programming ----------------------


def buildMaxMat(T):
    l = len(T)
    c = len(T[0])
    M = matrix.init(l, c, 0)

    for j in range(c):
        M[0][j] = T[0][j]

    for i in range(1, l):
        M[i][0] = T[i][0] + max(M[i-1][0], M[i-1][1])
        for j in range(1, c-1):
            M[i][j] = T[i][j] + max(M[i-1][j-1], M[i-1][j], M[i-1][j+1])
        M[i][c-1] = T[i][c-1] + max(M[i-1][c-2], M[i-1][c-1])
    
    return M
    
@timing.timing
def HarryPotter(T):
    M = buildMaxMat(T)
    n = len(M)  # line nb
    return M[n-1][posMax(M[n-1])]
    


#----------------------------------------------------------------------
# Brut force... warning: can be long when l, c >= 15, 15

# without the path
def brut(T, i, j):
    if i == len(T)-1:
        return (T[i][j], [j])
    else:
        (m, L) = brut(T, i+1, j)
        if j > 0:
            (mleft, Lleft) = brut(T, i+1, j-1)
            if mleft > m:
                (m, L) = (mleft, Lleft)
        if j < len(T[0]) - 1:
            (mright, Lright) = brut(T, i+1, j+1)
            if mright > m:
                (m, L) = (mright, Lright)
        return (m + T[i][j], [j] + L)
@timing.timing
def HarryPotterBrutForce(T):
    maxi = 0
    for j in range(len(T[0])):
        m, L =  brut(T, 0, j)
        if m > maxi:
            maxi = m
            Lmax = L
    return maxi, Lmax
    
# with the path        
def brut2(T, i, j):
    if i == len(T)-1:
        return (T[i][j], [j])
    else:
        (m, L) = brut2(T, i+1, j)
        if j > 0:
            (mleft, Lleft) = brut2(T, i+1, j-1)
            if mleft > m:
                m = mleft
                L = Lleft
        if j < len(T[0]) - 1:
            (mright, Lright) = brut2(T, i+1, j+1)
            if mright > m:
                m = mright
                L = Lright
        return (m + T[i][j], [j] + L)


def HarryPotterBrutForce2(T):
    
    maxi = 0
    for j in range(len(T[0])):
        m, L = brut2(T, 0, j)
        if m > maxi:
            maxi, Lmax = m, L
    return maxi, Lmax

#-----------------------------------------------------------------------
# some examples to test


HP15 = matrix.loadMatrix("files/HarryPotter15.txt") # 129
HP20 = matrix.loadMatrix("files/HarryPotter20.txt") # 1676
HP50 = matrix.loadMatrix("files/HarryPotter50.txt") # 4200
#
