#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AVL: insertion & deletion
"""

from algopy import avl



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

"""
insertion
"""

def __insertAVL(A, x):
    if A == None:
        return (avl.AVL(x, None, None, 0), True)
    elif x == A.key:
        return (A, False)
    else:
        if x < A.key:
            (A.left, dh) = __insertAVL(A.left, x)
            if not dh:
                return (A, False)
            else:
                A.bal += 1
                if A.bal == 0:
                    return (A, False)
                elif A.bal == 1:
                    return (A, True)
                else: # A.bal == 2
                    if A.left.bal == 1:
                        print("rr", A.key)
                        A = rr(A)
                    else:
                        print("lrr", A.key)
                        A = lrr(A)
                    return (A, False)
        else:   # x > A.key
            (A.right, dh) = __insertAVL(A.right, x)
            if not dh:
                return (A, False)
            else:
                A.bal -= 1
                if A.bal == 0:
                    return (A, False)
                elif A.bal == -1:
                    return (A, True)
                else:
                    if A.right.bal == -1:
                        print("lr", A.key)
                        A = lr(A)
                    else:
                        print("rlr", A.key)
                        A = rlr(A)
                    return (A, False)
                    
            
            
def insertAVL(A, x):
    (A, dh) = __insertAVL(A, x)
    return A
        

def buildAVLfromList(L, A = None):
    for x in L:
        A = insertAVL(A, x)
    return A


L1 = [13, 20, 5, 1, 15, 10, 18, 25, 4, 21, 27, 7, 12]
L2 = [21, 7, 33, 5, 17, 26, 47, 1, 9, 20, 31, 42, 53, 4, 15]
L3 = [-15, -2, 0, 5, 8, 25, 32, 42, 51, 66]
L_tuto = [17, 9, 29, 3, 13, 23, 40, 1, 8, 11, 42]
L_exam = [25, 60, 35, 10, 20, 5, 70, 65, 45]


"""
deletion
"""

# non optimized

def maxBST(B):
    while B.right != None:
        B = B.right
    return B.key
    
def __deleteAVL(x, A):
    if A == None:
        return (None, False)
        
    elif x == A.key:
        if A.left != None and A.right != None:
            A.key = maxBST(A.left)
            x = A.key   # to use the case <=
        else:
            if A.left == None:
                return(A.right, True)
            else:
                return(A.left, True)
                
    if x <= A.key:      
        (A.left, dh) = __deleteAVL(x, A.left)
        if not dh:
            return (A, False)
        else:
            A.bal -= 1              # long version
            if A.bal == 0:
                return (A, True)
            elif A.bal == -1:
                return (A, False)
            else:   # A.bal == -2
                if A.right.bal == -1:
                    A = lr(A)
                    return (A, True)
                elif A.right.bal == 0:
                    A = lr(A)
                    return (A, False)
                else:
                    A = rlr(A)
                    return (A, True)
           
    else:   # x > A.key
        (A.right, dh) = __deleteAVL(x, A.right)
        if not dh:
            return (A, False)
        else:
            A.bal += 1
            if A.bal == 2:
                if A.right.bal == -1:
                    A = lrr(A)
                else:
                    A = rr(A)
            return (A, A.bal == 0)  # this shortcut also works in previous case!

def deleteAVL(x, A):
    (A, _) = __deleteAVL(x, A)
    return A


# optimization ?
#  maxAVL can include deletion, balance factor updates and possible rebalancing
# -> no need to make a recursive call in __deleteAVL


def delMaxAVL(A):
    if A.right == None:
        return (A.key, A.left, True)
    else:
        (m, A.right, dh) = delMaxAVL(A.right)
        if dh:
            A.bal += 1
            if A.bal == 2:
                if A.left.bal == -1:
                    A = lrr(A)
                else:
                    A = rr(A)
            return (m, A, A.bal == 0)
        else:
            return (m, A, False)
            
# final version!            
def del_min_avl(A):
    if A.left == None:
        return (A.right, True)
    else:
        (A.left, dh) = del_min_avl(A.left)
        if dh:
            A.bal -= 1
            if A.bal == -2:
                if A.left.bal == +1:
                    A = rlr(A)  # rdg(A)
                else:
                    A = lr(A)   # rg(A)
            return (A, A.bal == 0)
        else:
            return (A, False)            

# long version
def del_min_avl2(A):
    if A.left == None:
        return (A.right, True)
    else:
        (A.left, dh) = del_min_avl2(A.left)
        if not dh:
            return (A, False)
        else:
            A.bal -= 1
            if A.bal == 0:
                return (A, True)
            elif A.bal == -1:
                return (A, False)
            else:   # A.bal == -2
                if A.right.bal == -1:
                    A = lr(A)   # rg(A)
                    return (A, True)
                elif A.right.bal == 0:
                    A = lr(A)   # rg(A)
                    return (A, False)
                else:
                    A = rlr(A)  # rdg(A)
                    return (A, True)
            
# other optimizations?
# - in case of a double node: 
#   we choose between the left subtree maximum and the right subtree minimum
#   depending on the balance factor

        