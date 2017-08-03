# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 15:18:59 2017

@author: DUCK HA HWANG
"""
"""
Question 4
Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is an ancestor of both nodes. 
For example, the root is a common ancestor of all nodes on the tree, 
but if both nodes are descendents of the root's left child, 
then that left child might be the lowest common ancestor. 
You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. 
The function definition should look like question4(T, r, n1, n2), 
where T is the tree represented as a matrix,
where the index of the list is equal to the integer stored in that node and a 1 represents a child node,
r is a non-negative integer representing the root, 
and n1 and n2 are non-negative integers representing the two nodes in no particular order. 
For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
"""

# A recursive python program to find LCA of two nodes
# n1 and n2
 
# A Binary tree node
def left_tree(T,current_node):
    i = current_node
    check=True
    while check:
        i-=1
        if T[current_node][i] == 1:
            check=False
   
    return i    
    
def right_tree(T,current_node):
    i = current_node
    check=True
    while check:
        i+=1
        if T[current_node][i] == 1:
            check=False
   
    return i 

# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def question4(T,r, n1, n2):
    """
    :type T: 2D matirix
    :type r: int
    :type n1: int
    :type n2: int
    :rtype: int
    """
    
    # Base Case
    if r is None:
        return None

    while (r < n1 or r > n2):
        # If both n1 and n2 are smaller than root, then the functuntion lies in left again
        if(r > n1 and r > n2):
            r= left_tree(T,r)
        # If both n1 and n2 are greater than root, then functuntion lies in right again    
        if(r < n1 and r < n2):
            r= right_tree(T,r)
    
#==============================================================================
#     # If both n1 and n2 are smaller than root, then the functuntion lies in left again
#     if(r > n1 and r > n2):
#         return question4(T,left_tree(T,r), n1, n2)
#  
#     # If both n1 and n2 are greater than root, then functuntion lies in right again
#     if(r < n1 and r < n2):
#         return question4(T,right_tree(T,r), n1, n2)
#==============================================================================
 
    return r

print "----test1----"
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                  3,
                  1,
                  4)

print "----test2----"
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]],
                  5,
                  3,
                  4)

print "----test2----"
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]],
                  5,
                  1,
                  6)