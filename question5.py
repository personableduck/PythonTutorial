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

#==============================================================================
# #Linked List Class
# class Node(object):
#   def __init__(self, data):
#     self.data = data
#     self.next = None
# 
# def question5(first_node,end_search):
#     """
#     :type first_node: liked list first node
#     :type end_search: int
#     :rtype: int
#     """
#     #base arrange data 
#     data_storage=[]
#     #change linked list to array data
#     readNode(node1,data_storage)
#     
#     #error case detector
#     if len(data_storage) - end_search < 0:
#         return False
#     
#     #simply index my location and return
#     return data_storage[len(data_storage) - end_search]
# 
# #return Linked List to array data    
# def readNode(node,data_storage):
#     data_storage.append(node.data)
#     if node.next != None:
#         readNode(node.next,data_storage)
#==============================================================================

# A complete working Python program to find length of a
# Linked List iteratively
 
# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null
 
 
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # This function is in LinkedList class. It inserts
    # a new node at the beginning of Linked List.
    def push(self, new_data):
        # 1 & 2: Allocate the Node &
        # Put in the data
        new_node = Node(new_data) 
        # 3. Make next of new Node as head
        new_node.next = self.head 
        # 4. Move the head to point to new Node
        self.head = new_node
        
    def add(self, new_data):

        new_node = Node(new_data) 
        # 3. Make next of new Node as head
        new_node.next = new_node
        # 4. Move the head to point to new Node
        self.head = new_node
 
 
    # This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.
    def getCount(self):
        temp = self.head # Initialise temp
        count = 0 # Initialise count
 
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count

def question5(ll,end_search):
    """
    :type first_node: liked list first node
    :type end_search: int
    :rtype: int
    """
    
    #Count my linked list node
    length_ll=ll.getCount()
    
    #error case detector
    if length_ll - end_search < 0:
        return False 
    
    #find my index location
    node_location= length_ll - end_search
    
    #Call first node
    current=ll.head
    
    #find linked list postion using index
    for i in range(node_location):
        current=current.next

    return current.data    
    

    
    
# Code execution starts here

print ""
print "Qestion5"
print ""
    
print "----Q5)test1----"

"""
Add a node at the front: 
The new node is always added before the head of the given Linked List. 
And newly added node becomes the new head of the Linked List. 
For example if the given Linked List is 10->15->20->25 and we add an item 5 at the front, 
then the Linked List becomes 5->10->15->20->25. 
Let us call the function that adds at the front of the list is push(). 
The push() must receive a pointer to the head pointer, 
because push must change the head pointer to point to the new node
"""

llist=LinkedList()
llist.push(11)
llist.push(12)
llist.push(13)
llist.push(14)
llist.push(15)

print question5(llist, 3)    
    
print "----Q5)test2----" 

llist=LinkedList()
llist.push(23)
llist.push(12)
llist.push(13)
llist.push(2)
llist.push(4)
llist.push(5)
llist.push(100)

print question5(llist, 2) 

print "----Q5)test3----"  

llist=LinkedList()
llist.push(55)
llist.push(52)
llist.push(36)
llist.push(21)
llist.push(41)
llist.push(52)
llist.push(120)
llist.push(114)
llist.push(150)
llist.push(610)

print question5(llist, 4)

print "----Q5)test4----"  

llist=LinkedList()
llist.push(5)    
    
print question5(llist, 4)