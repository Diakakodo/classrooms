#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
November 2018
BST: S2#-API
"""

from algopy import bintree

# BST -> list
def __bst2list(B, L):
    if B != None:
        __bst2list(B.left, L)
        L.append(B.key)
        __bst2list(B.right, L)
        

def bst2list(B):
    L = []
    __bst2list(B, L)
    return L


# list -> BST: warning, works only with strictly increasing lists!
# warning: we work on [left, right[ here!

def __list2bst(L, left, right):
    if left == right:
        return None
    else:
        mid = left +  (right - left) // 2
        B = bintree.BinTree(L[mid], None, None)
        B.left = __list2bst(L, left, mid)
        B.right = __list2bst(L, mid+1, right)
        return B
    
#or
def __list2bst(L, left, right):
    if left == right:
        return None
    else:
        mid = left +  (right - left) // 2
        return bintree.BinTree(L[mid], 
                               __list2bst(L, left, mid), 
                               __list2bst(L, mid+1, right))

    
def list2bst(L):
    return __list2bst(L, 0, len(L))
    
    


# bonus: try to avoid the problem with not strictly increasing lists
# first version: with an "ugly" loop... (a nicer version?)

def __list2bst2(L, left, right):
    if left == right:
        return None
    else:
        mid = left +  (right - left) // 2
        while mid < right - 1 and L[mid] == L[mid + 1]:
            mid += 1
        return bintree.BinTree(L[mid], 
                               __list2bst2(L, left, mid), 
                               __list2bst2(L, mid+1, right))

    
def list2bst2(L):
    return __list2bst2(L, 0, len(L))
    
    
# test

def __testbst(B, inf, sup):
    if B == None:
        return True
    else:
        if B.key > inf and B.key <= sup:
            return __testbst(B.left, inf, B.key) \
                    and __testbst(B.right, B.key, sup)
        else:
            return False
        

def testbst(B):
    return __testbst(B, -float('inf'), float('inf'))


# Researches

def minBST(B):
    """
    B != None
    """
    if B.left == None:
        return B.key
    else:
        return minBST(B.left)
    
def maxBST(B):
    """
    B != None
    """
    while B.right != None:
        B = B.right
    return B.key


def searchBST(B, x):
    if B == None or B.key == x:
        return B
    else:
        if x < B.key:
            return searchBST(B.left, x)
        else:
            return searchBST(B.right, x)

def searchBST_iter(B, x):
    while B != None and B.key != x:
        if x < B.key:
            B = B.left
        else:
            B = B.right
    return B

# insertions


def leaf_insert(B, x):
    if B == None:
        return bintree.BinTree(x, None, None)
    else:
        if x <= B.key:
            B.left = leaf_insert(B.left, x)
        else:
            B.right = leaf_insert(B.right, x)
        return B

def leaf_insert_iter(B, x):
    new = bintree.BinTree(x, None, None)
    P = None
    T = B
    while T != None:
        P = T
        if x <= T.key:
            T = T.left
        else:
            T = T.right
    
    if P == None:
        return new
    else:
        if x <= P.key:
            P.left = new
        else:
            P.right = new
        return B
    


 
