# -*- coding: utf-8 -*-
"""
Philosophers Stone
Oct. 2018
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

#@timing.timing
def HarryPotterGreedy(T):
    j = posMax(T[0])
    s = T[0][j]
    for i in range(1, len(T)):
        m = j    # m = position of the supposed maximum
        #FIXME
        
        s += T[i][m]
        j = m
        
    return s



#----------------- Dynamic Programming ----------------------


def buildMaxMat(T):
    #??????
    pass

#@timing.timing
def HarryPotter(T):
    M = buildMaxMat(T)
    n = len(M)  # line nb
    return M[n-1][posMax(M[n-1])]
    


#----------------------------------------------------------------------
# Brut force... warning: can be long when l, c >= 15, 15

# without the path
def brut(T, i, j):
    if i == len(T)-1:
        return T[i][j]
    else:
        #FIXME 
        pass
    
    
#@timing.timing
def HarryPotterBrutForce(T):
    
    maxi = 0
    for j in range(len(T[0])):
        maxi = max(maxi, brut(T, 0, j))
    return maxi
    

#-----------------------------------------------------------------------
# some examples to test


HP15 = matrix.loadMatrix("files/HarryPotter15.txt") # 129
HP20 = matrix.loadMatrix("files/HarryPotter20.txt") # 1676
HP50 = matrix.loadMatrix("files/HarryPotter50.txt") # 4200

def test(HP):
    HarryPotterGreedy(HP)
    HarryPotter(HP)
    HarryPotterBrutForce(HP)

'''    
Results:
>>> test(HP15)
HarryPotterGreedy function tooks 0.0 ms
buildMaxMat function tooks 0.0 ms
HarryPotterBrutForce function tooks 32824.61190223694 ms

>>> test(HP20)
HarryPotterGreedy function tooks 0.0 ms
buildMaxMat function tooks 0.0 ms
HarryPotterBrutForce function tooks 11073955.830097198 ms (> 3h)

>>> HarryPotterGreedy(HP50)
HarryPotterGreedy function tooks 0.0 ms
>>> HarryPotter(HP50)
HarryPotter function tooks 15.59591293334961 ms
'''
