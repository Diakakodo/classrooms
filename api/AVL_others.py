# -*- coding: utf-8 -*-
"""
S2-API - 2018
AVL: others
"""

from algopy import bintree, avl

def __list2AVL(L, left, right):
    """
    L[left, right[ -> AVL
    """
    if left >= right:
        return None
    else:
        mid = left + (right-left) // 2
        A = avl.AVL(L[mid], None, None, 0)
        if right - left == 2:
            A.bal = 1
        A.left = __list2AVL(L, left, mid)
        A.right = __list2AVL(L, mid + 1, right)
        return A

def sorted_list2AVL2(L):
    return __list2AVL(L, 0, len(L))


def __toAVL(B):
    """
    returns (AVL, height)
    """
    if B == None:
        return (None, -1)
    else:
        A = avl.AVL(B.key, None, None, 0)
        (A.left, hleft) = __toAVL(B.left)
        (A.right, hright) = __toAVL(B.right)
        A. bal = hleft - hright
        return (A, 1 + max(hleft, hright))
        
def toAVL(B):
    (A, _) = __toAVL(B)
    return A


#------------------------------------------------------------------------------
# height-balanced test

def __isbalanced(B):
    if B == None:
        return (-1, True)
    else:
        (hl, test) = __isbalanced(B.left) 
        if not test:
            return (0, False)
        else:
            (hr, test) = __isbalanced(B.right)
            return (1 + max(hl, hr), test and abs(hl-hr) < 2)
                
                
def isbalanced(B):
    (_, result) = __isbalanced(B)
    return result

#------------------------------------------------------------------------------
# full test

infty = float('inf')

def testAVL(B, inf, sup):
    if B == None:
        return (-1, True)
    elif B.key < inf or B.key > sup:
        return (0, False)
    else:
        (hl, test) = testAVL(B.left, inf, B.key) 
        if not test:
            return (0, False)
        else:
            (hr, test) = testAVL(B.right, B.key, sup)
            return (1 + max(hl, hr), test and abs(hl-hr) < 2)
                
                
def isAVL(B):
    (h, result) = testAVL(B, -infty, infty)
    return result    