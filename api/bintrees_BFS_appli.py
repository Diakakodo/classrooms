# -*- coding: utf-8 -*-
"""
S2# - API - Nov. 2018
BinTree: BFS and applications

"""

from algopy import bintree, queue


"""
BFS: Breadth-First Search (largeur)
"""

#simple: displays keys

def bfs(B): 
    if B != None:
        q = queue.Queue()
        q.enqueue(B)
        while not q.isempty():
            B = q.dequeue()
            print(B.key, end= ' ')
            if B.left != None:
                q.enqueue(B.left)
            if B.right != None:
                q.enqueue(B.right)

# with level change marks (None): displays keys by levels
def bfs_levels(B):
    if B:
        q = queue.Queue()
        q.enqueue(B)
        q.enqueue(None)
        while not q.isempty():
            B = q.dequeue()
            if B == None:
                print()
                if not q.isempty():
                    q.enqueue(None)
            else:
                print(B.key, end=' ')
                if B.left:
                    q.enqueue(B.left)
                if B.right:
                    q.enqueue(B.right)

# another way to manage levels, with two queues.                    
def width(B): 
    """
    computes the width of a bintree
    """
    w_max = 0
    if B != None:
        q = queue.Queue() #current
        q.enqueue(B)
        q_next = queue.Queue() #next level
        w = 0
        while not q.isempty():
            B = q.dequeue()
            w = w + 1
            if B.left != None:
                q_next.enqueue(B.left)
            if B.right != None:
                q_next.enqueue(B.right)
            if q.isempty():
                w_max = max(w, w_max)
                w = 0
                (q, q_next) = (q_next, q)
    return w_max
    
#------------------------------------------------------------------
    
def is_perfectBFS(B): # complet!
    """
    BFS: tests if each level has twice as many nodes 
    as the previous level
    """
    if B == None:
        return True
    else:
        q = queue.Queue()
        q.enqueue(B)
        q.enqueue(None)
        ok = True
        (current, expected) = (0, 1)
        while not q.isempty() and ok:
            B = q.dequeue()
            if B == None:
                ok = (current == expected)
                if not q.isempty():
                    q.enqueue(None)  
                    (expected, current) = (2 * current, 0)
            else:
                current += 1
                if B.left != None:
                    q.enqueue(B.left)
                if B.right != None:
                    q.enqueue(B.right)
        return ok
        
#------------------------------------------------------------------

def is_complete(B): # parfait !
    if B == None:
        return True
    else:
        q = queue.Queue()
        q.enqueue(B)
        emptychild = False
        while not emptychild:
            T = q.dequeue()
            if T.left == None:
                emptychild = True
            else:
                q.enqueue(T.left)
                if T.right != None:
                    q.enqueue(T.right)
                else:
                    emptychild = True
        complete = (T.right == None)
        while not q.isempty() and complete:
            T = q.dequeue()
            complete = (T.left == T.right)
        return complete