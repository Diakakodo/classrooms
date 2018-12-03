#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:11:21 2017
@author: nathalie
"""

from algopy import avl, bintree

#------------------------------------------------------------------------------    
# rotations: works only in "usefull" cases

def lr(A): # rotation gauche
    aux = A.right
    A.right = aux.left
    aux.left = A
    aux.bal += 1
    A.bal = -aux.bal
    return aux

def rr(A): # rotation droite
    aux = A.left
    A.left = aux.right
    aux.right = A
    aux.bal -= 1
    A.bal = -aux.bal
    return aux

def lrr(A): # rotation gauche-droite
# left rotation on left child
    aux = A.left.right
    A.left.right = aux.left
    aux.left = A.left
# right rotation
    A.left = aux.right
    aux.right = A
    A = aux

    if A.bal == -1:
        (A.left.bal, A.right.bal) = (1, 0)
    elif A.bal == 1:
        (A.left.bal, A.right.bal) = (0, -1)
    else:
        (A.left.bal, A.right.bal) = (0, 0)
    A.bal = 0
    
    return A

def rlr(A): # rotation droite-gauche
    aux = A.right.left
    A.right.left = aux.right
    aux.right = A.right
    
    A.right = aux.left
    aux.left = A
    
    (aux.left.bal, aux.right.bal) = (0, 0)
    if aux.bal == -1:
        aux.left.bal = 1
    elif aux.bal == 1:
        aux.right.bal = 1
    aux.bal = 0

    return aux

#------------------------------------------------------------------------------
# insertion

def __insertAVL(x, A):
    if B == None:
        return (avl.AVL(x, None, None, 0), True)
    else:
        if x < A.key:
            (A.left, dh) = __insertAVL(x, A.left)
        
        
        elif x > A.key:
            (A.right, dh) = __insert(x, A.left)
    
    
    
    
    
    
def insertAVL(x, A):
    (A, dh) = __insertAVL(x, A)
    return A
        




