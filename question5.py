# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 17:07:40 2017

@author: DUCK HA HWANG

Question 5
Find the element in a singly linked list that's m elements from the end. 
For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. 
The function definition should look like question5(ll, m), 
where ll is the first node of a linked list and m is the "mth number from the end". 
You should copy/paste the Node class below to use as a representation of a node in the linked list. 
Return the value of the node at that position.
"""

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def question5(first_node,end_search):
    data_storage=[]
    readNode(node1,data_storage)
    
    return data_storage[len(data_storage) - end_search]
    
def readNode(node,data_storage):
    data_storage.append(node.data)
    if node.next != None:
        readNode(node.next,data_storage)


    
print "----test1----"  

node1 = Node(11)
node2 = Node(12)
node3 = Node(13)
node4 = Node(14)
node5 = Node(15)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print question5(node1, 3)

print "----test2----"  

node1 = Node(23)
node2 = Node(12)
node3 = Node(13)
node4 = Node(2)
node5 = Node(4)
node6 = Node(5)
node7 = Node(100)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

print question5(node1, 6)

print "----test3----"  

node1 = Node(5)
node2 = Node(52)
node3 = Node(36)
node4 = Node(21)
node5 = Node(41)
node6 = Node(52)
node7 = Node(120)
node8 = Node(114)
node9 = Node(150)
node10 = Node(610)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10

print question5(node1, 4)