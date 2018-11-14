#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 16:50:32 2018

@author: nathalie
"""

from algopy import bintree

def size(B):
    if B == None:
        return 0
    else:
        return 1 + size(B.left) + size(B.right)
    
def height(B):
    if B == None:
        return -1
    else:
        return 1 + max(height(B.left), height(B.right))

def myprint(x):
    print(x, end='')
    
def DFS(B):
    if B == None:
        myprint('_')
    else:
        myprint('<' + str(B.key) + ',')
        DFS(B.left)
        myprint(',')
        DFS(B.right)
        myprint('>')
        
def DFSstr(B):
    if B == None:
        return '_'
    else:
        s = '<' + str(B.key) + ','
        s += DFSstr(B.left)
        s += ','
        s += DFSstr(B.right)
        s += '>'
        return s


##############################################################################

"""
Arbres d'expressions
"""

def tree2exp(B):
    """
    B != None
    all internal nodes are double
    """
    if B.left == None:
        return B.key
    else:
        exp = '('
        exp += tree2exp(B.left)
        exp += B.key
        exp += tree2exp(B.right)
        exp += ')'
    return exp

def nodes(B):
    if B.left == None:
        return (0, 1)
    else:
        (op_left, val_left) = nodes(B.left)
        (op_right, val_right) = nodes(B.right)
        return (op_left + op_right + 1, 
                val_left + val_right)



##############################################################################

# ex 1.3

def __pme(B, prof = 0):    
    if B == None:
        return ???
    elif B.left == None and B.right == None:
        return ???
    else:
        
        ?? = __pme(B.left, prof+1)
        ?? = __pme(B.right, prof+1)
        return ???

    
def pme(B):
    if B == None:
        return 0
    else:
        (lce, nbf) = __pme(B)
        return lce / nbf
        
