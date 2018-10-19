# -*- coding: utf-8 -*-
"""
Oct 2018
B-trees - classics: search + insert + delete
"""

from algopy import btree

# 2.1: min and mx

def minBTree(B):
    '''
    B is not empty
    '''
    while B.children != []:
        B = B.children[0]
    return B.keys[0]
    

def maxBTree(B):
    while B.children:
        B = B.children[B.nbkeys]  # B.children[-1]
    return B.keys[B.nbkeys-1]   # B.keys[-1]
    
# 2.2: Searching


def __binarySearchPos(L, x, left, right):
    if left >= right:
        return right
    else:
        mid = left + (right - left) // 2
        if x == L[mid]:
            return mid
        elif x < L[mid]:
            return __binarySearchPos(L, x, left, mid)
        else:
            return __binarySearchPos(L, x, mid + 1, right)
    
def binarySearchPos(L, x):
    """
    returns the position where x is or might be in L
    """
    return __binarySearchPos(L, x, 0, len(L))

def _searchBTree(B, x):                                       
    i = binarySearchPos(B.keys, x)
    if i < B.nbkeys and B.keys[i] == x:
        return (B, i)
    else:
        if B.children == []:
            return None
        else:
            return _searchBTree(B.children[i], x)
    
    
def searchBTree(B, x):
    if B == None:
        return None
    else:
        return _searchBTree(B,x)



# 2.3 insertion

def split(B, i):
    '''
    splits the child i of B
    conditions:
    - B is a nonempty tree and its root is not a 2t-node.
    - The child i of B exists and its root is a 2t-node.
    '''
    L = B.children[i]
    R = btree.BTree()
    #FIXME
    pass
    
def __insert(B, x):
    '''
    conditions:
    - B is a nonempty tree 
    - its root is not a 2t-node
    '''
    i = binarySearchPos(B.keys, x)
    #FIXME
    pass
        
def insert(B, x):
    #FIXME
    pass

###########################################################################            
# deletion
            
#-------------------------------------------------------------------------
# rotations (generalized)

def leftRotation(B, i):
    '''
    makes a rotation from child i+1 to child i
    Conditions: 
    - the tree B exists, 
    - its child i exists and its root is not a 2t-node, 
    - its child i+1 exists and its root is not a t-node.
    '''
    L = B.children[i]
    R = B.children[i+1]

    #FIXME


def rightRotation(B, i):
    '''
    makes a rotation from child i-1 to child i
    Conditions: 
    - the tree B exists, 
    - its child i exists and its root is not a 2t-node, 
    - its child i-1 exists and its root is not a t-node.
    '''
    L = B.children[i-1]
    R = B.children[i]

    # FIXME
        

#------------------------------------------------------------------------------
# merge
def merge(B, i):
    '''
    merge B children i and i+1 into child i
    Conditions: 
    - the tree B exists and its root is not a t-node,
    - children i and i+1 exist and their roots are t-nodes.
    '''
    L = B.children[i]
    R = B.children.pop(i+1) #B.children[i+1]
    
    #FIXME
            
#-------------------------- delete --------------------------------------------
def __delete(B, x):
    i = binarySearchPos(B.keys, x)
    #FIXME


def delete(B, x):
    if B != None:
        __delete(B, x)
        #FIXME