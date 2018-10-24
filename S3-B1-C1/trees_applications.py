# -*- coding: utf-8 -*-
"""
Sep 2018
S3 - trees part 3
"""

from algopy import tree
from algopy import treeasbin

'''
tree -> prefix-suffix vector
'''

def __prefsuff(T, L):
    L.append(T.key)
    for child in T.children:
        __prefsuff(child, L)
    L.append(T.key)
    
def __prefsuffbin(B, L):
    L.append(B.key)
    C = B.child
    while C != None:
        __prefsuffbin(C, L)
        C = C.sibling
    L.append(B.key)

def __prefsuffbin2(B, L):
    L.append(B.key)
    if B.child != None:
        __prefsuffbin2(B.child, L)
    L.append(B.key)
    if B.sibling != None:
        __prefsuffbin2(B.sibling, L)

def prefsuff(T):
    L = []
    if type(T) == tree.Tree:
        __prefsuff(T, L)
    else:
        __prefsuffbin(T, L)
    return L

'''
tree -> list representation
'''

def tree2list(T):
    s = '(' + str(T.key)
    for child in T.children:
        s += tree2list(child)
    s += ')'
    return s

def treeAsBin2list(B):
    s = '(' + str(B.key)
    C = B.child
    while C != None:
        s += treeAsBin2list(C)
        C = C.sibling
    s += ')'
    return s
    
    
def treeAsBin2list2(B):
    s = '(' + str(B.key)
    if B.child:
        s += treeAsBin2list2(B.child)
    s += ')'
    if B.sibling:
        s += treeAsBin2list2(B.sibling)
    return s

'''
Average Arity: 
sum of the number of children per node divided by the number of internal nodes
from C3# 2018
'''


    
# with TreeAsBin
def __countnodestab(B):
    if B.child == None:
        return (0, 0)
    else:
        Bchild = B.child
        internnodes, nbchildren = 1, 0
        while Bchild != None:
            (nbi, nbc) = __countnodestab(Bchild)
            internnodes += nbi
            nbchildren += nbc + 1
            Bchild = Bchild.sibling
        return internnodes, nbchildren

def arityTAB(B):
    (nbi, nbc) = __countnodestab(B)
    return (nbc/nbi if nbi != 0 else 0)

#using the binary structure...
def __arity2(B):
    ''' 
    return (nb links, nb internal nodes)
    '''
    if B.child == None:
        (links, nodes) = (0, 0)
    else:
        (l, n) = __arity2(B.child)
        (links, nodes) = (l + 1, n + 1)
        
    if B.sibling != None:
        (l, n) = __arity2(B.sibling)
        links += l + 1
        nodes += n

    return (links, nodes)

def averagearity_bin2(B):
    (links, nodes) = __arity2(B)
    return 0 if nodes == 0 else links / nodes


# with "classical" implem (not in tutorial)
def __countnodes(T):
    """
    returns (nb internal nodes, nb children)
    """
    if T.nbchildren == 0:
        return (0, 0)
    internnodes = 1
    nbchildren = T.nbchildren
    for child in T.children:
        (nbi, nbc) = __countnodes(child)
        internnodes += nbi
        nbchildren += nbc
    return (internnodes, nbchildren)
        
        
def arity(T):
    (nbi, nbc) = __countnodes(T)
    return (nbc/nbi if nbi != 0 else 0)
    
"""
tree -> dot
"""

from  algopy import queue

def dot(T):
    """Write down dot format of tree.

    Args:
        ref (Tree).

    Returns:
        str: String storing dot format of tree.

    """

    s = "graph {\n"
    s += "node [shape=circle, fixedsize=true, height=0.5, width=0.5]\n"
    q = queue.Queue()
    q.enqueue(T)
    while not q.isempty():
        T = q.dequeue()
        for child in T.children:
            s = s + "   " + str(T.key) + " -- " + str(child.key) + "\n"
            q.enqueue(child)
    s += "}"
    return s

  

"""
TreeAsBin -> Tree
"""

def treeasbin2tree(B):
    T = tree.Tree(B.key, [])
    child = B.child
    while child != None:
        T.children.append(treeasbin2tree(child))
        child = child.sibling
    return T

# using binary structure
    
def __treeasbin2tree2(B, parent):
    '''
    convert B -> added as new child of parent
    '''
    newChild = tree.Tree(B.key)
    parent.children.append(newChild)
    if B.sibling:
        __treeasbin2tree2(B.sibling, parent)
    if B.child:
        __treeasbin2tree2(B.child, newChild)

def treeasbin2tree2(B):
    T = tree.Tree(B.key)
    if B.child:
        __treeasbin2tree2(B.child, T)
    return T
    
"""
Tree -> TreeAsBin
"""

def treeToTreeAsBin(T):
    B = treeasbin.TreeAsBin(T.key, None, None)
    if T.nbchildren != 0:
        B.child = treeToTreeAsBin(T.children[0])
        S = B.child
        for i in range(1, T.nbchildren):    
            S.sibling = treeToTreeAsBin(T.children[i])
            S = S.sibling
    return B

def tree2TreeAsBin(T):
    B = treeasbin.TreeAsBin(T.key, None, None)
    firstchild = None
    for i in range(T.nbchildren-1, -1, -1):
        C = tree2TreeAsBin(T.children[i])
        C.sibling = firstchild
        firstchild = C
    
    B.child = firstchild
    return B

# using binary structure
def __tree2tab(parent, i):
    '''
    build child #i of parent
    '''
    if i == parent.nbchildren:
        return None
    else:
        child_i = treeasbin.TreeAsBin(parent.children[i].key)
        child_i.sibling = __tree2tab(parent, i+1)
        child_i.child = __tree2tab(parent.children[i], 0)
        return child_i
    
def treeToTAB(T):
    return treeasbin.TreeAsBin(T.key, __tree2tab(T, 0), None)



"""
list -> tree (int keys)
"""

def __list2tree(s, i=0): 
        i = i + 1 # to skip the '('
        key = ""
        while s[i] != '(' and s[i] != ')':  # s[i] not in "()"
            key += s[i]
            i += 1
        T = tree.Tree(int(key), [])
        while s[i] != ')':
            (C, i) = __list2tree(s, i)
            T.children.append(C)
        i += 1
        return (T, i)

def list2tree(L):
    (T, _) = __list2tree(L)
    return T


def __list2treeasbin(s, i=0): 
    if i < len(s) and s[i] == '(':   
        i = i + 1 # to pass the '('
        key = ""
        while not (s[i] in "()"):
            key = key + s[i]
            i += 1
        B = treeasbin.TreeAsBin(int(key))
        (B.child, i) = __list2treeasbin(s, i)
        i = i + 1   # to pass the ')'
        (B.sibling, i) = __list2treeasbin(s, i)
        return (B, i)
    else:
        return (None, i)

def list2treeasbin(s):
    return __list2treeasbin(s)[0]


"(15(3(-6)(10))(8(11(0)(4))(2)(5))(9))"
        
