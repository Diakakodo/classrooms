# -*- coding: utf-8 -*-
"""
Matrices: maths and tests
@author: Nathalie
"""

from algopy import matrix

        
"""

# parcours complet dans tous les cas : 
(l, c) = (len(M), len(M[0]))
for i in range(l):
    for j in range(c):
        M[i][j]...


# parcours interrompu:
(l, c) = (len(M), len(M[0]))
i = 0
while i < l and ???:
    j = 0
    while j < c and ???:
        M[i][j]....
        j += 1
    i += 1
"""    
    
#--------------------------------------------------------------------
# 1.3 - 1.4 mathematical operations
# matrices are not empty!
        
def matrixaddition(A, B):
    (l, c) = (len(A), len(A[0]))
    if (l,c) != (len(B), len(B[0])):
        raise Exception("Matrices have not same dimensions")
    M = matrix.init(l, c, 0)
    for i in range(l):
        for j in range(c):
            M[i][j] = A[i][j] + B[i][j]
    return M





#--------------------------------------------------------------------
# 2.1 research
# matrix is not empty!

# in two functions:
def searchMatrix(M, x):
    (i, lin, col) = (0, len(M), len(M[0]))
    found = -1
    while i < lin and found == -1:
        j = 0
        while j < col and M[i][j] != x:
            j += 1
        if j != col:
            found = j
        i += 1
    if found != -1:
        return (i-1, found)
    else:
        return (-1, -1)
        
# two functions:
def __searchList(L, n, x):
    """
    search position of x in L of length n
    """
    j = 0
    while j < n and L[j] != x:
        j += 1
    if j == n:
        return -1
    else:
        return j

def searchMatrix2(M, x):
    (lin, col) = (len(M), len(M[0]))
    i = 0
    found = -1
    while i < lin and found == -1:
        found = __searchList(M[i], col, x)
        i += 1
    if found != -1:
        return (i-1, found)
    else:
        return (-1, -1)        

#------------------------------------------------------------------------------
#                   vertical symmetry

M_vsym = [[1, 1, 10, 10, 7],
          [10, 0, 9, 3, 8],
          [3, 1, 4, 7, 5],
          [0, 8, 1, 1, 1],
          [3, 1, 4, 7, 5],
          [10, 0, 9, 3, 8],
          [1, 1, 10, 10, 7]]
          
M_not_vsym = [[1, 1, 10, 10, 7],
              [10, 0, 9, 3, 8],
              [3, 1, 4, 7, 5],
              [0, 8, 1, 1, 1],
              [3, 1, 4, 7, 5],
              [10, 0, 9, 3, 8],
              [1, 1, 10, 10, 6]]
              
M_vsym2 = [[1, 1, 10, 10, 7],
           [10, 0, 9, 3, 8],
           [3, 1, 4, 7, 5],
           [3, 1, 4, 7, 5],
           [10, 0, 9, 3, 8],
           [1, 1, 10, 10, 7]]


def __equal(L1, L2):
    i = 0
    n = len(L1)
    while i < n and L1[i] == L2[i]:
        i += 1
    return i == n

def vsymmetric(M):
    n = len(M)
    i = 0
    while i < n // 2 and __equal(M[i], M[n-i-1]):
        i += 1
    return i == n // 2
       
        
        
# with a bool variable
def v_symmetric(M):
    (l, c) = (len(M), len(M[0]))
    
    i = 0
    test = True
    while i < l // 2 and test: 
        j = 0
        while j < c and test:
            test = (M[i][j] == M[l-i-1][j])
            j += 1
        i += 1
    return test
    
# without a bool variable
def v_symmetric2(M):
    (l, c) = (len(M), len(M[0]))
    ldiv2 = l // 2
    (i, j) = (0, c) 
    while i < ldiv2 and j == c: 
        j = 0
        while j < c and M[i][j] == M[l-i-1][j]:
            j += 1
        i += 1
    return j == c
    

# horizontal symmetry test

def symetric(M): 
    (l, c) = (len(M), len(M[0]))
    cdiv2 = c // 2
    j = 0
    stop = False
    while j < cdiv2 and not stop:
        i = 0
        while i < l and not stop:
            stop = (M[i][j] != M[i][c-j-1])
            i += 1
        j += 1
    return not stop

# two functions
def symList(L):
    """
    test whether L is symmetrical
    """
    i = 0
    n = len(L)
    while i < n//2 and L[i] == L[n-i-1]:
        i += 1
    return i == n // 2

def symmetrical(M):
    i = 0
    n = len(M)
    while i < n and symList(M[i]):
        i += 1
    return i == n


M_hsym = [[1, 10, 3, 0, 3, 10, 1], 
         [1, 0, 1, 8, 1, 0, 1], 
         [10, 9, 4, 1, 4, 9, 10], 
         [10, 3, 7, 1, 7, 3, 10], 
         [7, 8, 5, 1, 5, 8, 7]]


M_nothSym = [[1, 10, 3, 0, 3, 10, 1], 
         [1, 0, 1, 8, 1, 0, 1], 
         [10, 9, 4, 1, 4, 9, 10], 
         [10, 3, 7, 1, 7, 3, 10], 
         [7, 8, 5, 1, 5, 8, 6]]


M_hsym2 = [[1, 10, 3, 3, 10, 1], 
         [1, 0, 1, 1, 0, 1], 
         [10, 9, 4, 4, 9, 10], 
         [10, 3, 7, 7, 3, 10], 
         [7, 8, 5, 5, 8, 7]]