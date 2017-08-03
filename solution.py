# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 17:40:04 2017

@author: DUCK HA HWANG
"""

'''
-------------------------------------Question 1
'''

import unittest

class TestStringMethods(unittest.TestCase):

    def test(self):
        self.assertEqual(question1("udacity","ad"), True)

#==============================================================================
# def question1(str_word, sub):
#     
#     if str_word.find(sub) != -1:
#         return True
#     elif str_word[::-1].find(sub) != -1:
#         return True
#     else:
#         return False
#==============================================================================
    
def question1(s,t):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    #base case, if sub string is None then return False
    #if sub string is bigger than origin string return False
    if len(t) > len(s) or t == '':
        return False
    
    #find each charater with slice window method
    for i in range(len(t)):
        if s.find(t[i]) == -1:
            return False
        else:
            #delte finding character element to avoid repeat use
            s=s[:s.find(t[i])]+s[s.find(t[i])+1:]
    
    return True

print ""
print "Qestion1"
print ""

print "----Q1)test1----"     
s="udacity"
t="ad"
print question1(s,t)

print "----Q1)test2----" 
s="aaaacdddity"
t="ad"
print question1(s,t)

print "----Q1)test3----" 
s="Helloworld"
t="dlro"
print question1(s,t)

print "----Q1)test4----" 
s="Helloworld"
t="dlrol"
print question1(s,t)

print "----Q1)test5----" 
s="Helloworld"
t=""
print question1(s,t)

print "----Q1)test6----" 
s="Helloworld"
t="HHeeeewww"
print question1(s,t)

print "----Q1)test7----" 
s="Helloworld"
t="HHeelloworlddddd"
print question1(s,t)

if __name__ == '__main__':
    unittest.main()

'''
-------------------------------------Question 2
'''

def question_2(s):
    """
    :type s: str
    :rtype: str
    """
#==============================================================================
#     if s == "":
#         return ""
#==============================================================================
    
    ss=s[::-1] #Make reverse string set
    rtype=[]
    length_value_fix=len(s) 
    
    for index in range (length_value_fix):
        
        finding=s[index] #store index character from string    
        check_max=len(rtype)
        #if I can find any repeat character process find palindromic
        pass_flag=s[index+check_max:].find(finding) 
        
        if pass_flag != -1:
        
            while ss:      
                reversed_location=ss.find(finding)
                s_recall=ss[reversed_location:]
                s_reversed=s_recall[::-1]
                # Simply compare original string and reversed sting
                if s_recall == s_reversed:
                    if len(s_recall) > len(rtype) :    
                        rtype=s_recall
                    break
                else:
                    ss=s_recall[1:] #extract finding
                if len(ss) <= check_max:
                    break
        
        ss=s[index+1:length_value_fix]
        ss=ss[::-1]
    
    return rtype

print ""
print "Qestion2"
print ""
print "----Q2)test1----"  
a="babad"
print question_2(a)

print "----Q2)test2----" 
a="cbbd"
print question_2(a)

print "----Q2)test3----" 
a="budaaduudaaduc"
print question_2(a)

print "----Q2)test4----" 
a="cbbdbabadaaccccawreeeeeeeeeebdbdbdbbddbbcbadsadwqeo"
print question_2(a)

print "----Q2)test5----" 
a=""
print question_2(a)

'''
-------------------------------------Question 3
'''

def question3(G):
    """
    :type G: 2D array for Graph
    :rtype: dictionary
    """
    
    result ={} #This will store the result 
    G =  sorted(G,key=lambda item: item[2])   
    #root information
    root_diction={}    
    for node in range(len(G)):
        if G[node][0] not in root_diction:
            root_diction[G[node][0]]=G[node][0]
        if G[node][1] not in root_diction:      
            root_diction[G[node][1]]=G[node][1]
    #Uses union by rank)            
    rank={}
    for node in range(len(G)):
        if G[node][0] not in rank:
            rank[G[node][0]]=0
        if G[node][1] not in rank:      
            rank[G[node][1]]=0
    i = 0  # An index variable, used for sorted edges
    e = 0  # An index variable, used for result[]      
    while e < len(root_diction) -1 : 
        s,f,w =  G[i]
        #Using dictionary find adjacent list by union
        root_s=root_diction[s]
        if root_s != root_diction[root_s]:
            root_s = root_diction[root_s]   
        root_f=root_diction[f]
        if root_f != root_diction[root_f]:
            root_f = root_diction[root_f]
        #Compare union rank and root
        if root_s != root_f:
            #result dictionary format
            if s not in result:
                result[s]=[(f,w)]
            else:
                result[s].append((f,w))   
            if f not in result:
                result[f]=[(s,w)]
            else:
                result[f].append((s,w))
            
            #union update
            e+=1
            if rank[root_s] >= rank[root_f]:
                root_diction[f]=root_s
                root_diction[root_f]=root_s             
                if rank[root_f] == 0:
                    rank[root_s]+=1
                else:
                    rank[root_s]+=rank[root_f]+1
            else:
                root_diction[s]=root_f
                root_diction[root_s]=root_f
                            
                if rank[root_s] == 0:
                    rank[root_f]+=1
                else:
                    rank[root_f]+=rank[root_s]+1                      
        i = i + 1
        
    #print final result
    print result

print ""
print "Qestion3"
print ""
 
print "----Q3)test1----" 

G=[]
G.append(['a', 'b', 10])
G.append(['a', 'c', 6])
G.append(['a', 'd', 5])
G.append(['b', 'd', 15])
G.append(['c', 'd', 4])  
            
question3(G)

print "----Q3)test2----" 

G=[]
G.append(['A', 'B', 4])
G.append(['B', 'C', 8])
G.append(['C', 'D', 7])
G.append(['D', 'E', 9])
G.append(['E', 'F', 10])
G.append(['F', 'C', 4])
G.append(['F', 'D', 14])
G.append(['G', 'F', 2])
G.append(['G', 'H', 6])
G.append(['C', 'H', 2])
G.append(['G', 'I', 1])
G.append(['I', 'A', 8])
G.append(['I', 'B', 11])
G.append(['I', 'H', 7])

question3(G)       
        
print "----Q3)test3----"   

G=[]
G.append(['A', 'B', 4])
G.append(['B', 'C', 8])
G.append(['C', 'D', 7])
G.append(['D', 'A', 2])
G.append(['B', 'F', 10])
G.append(['C', 'H', 4])
G.append(['H', 'B', 14])
G.append(['G', 'A', 2])
G.append(['E', 'F', 6])
G.append(['I', 'K', 2])
G.append(['K', 'D', 1])
G.append(['F', 'K', 8])
G.append(['E', 'B', 11])
G.append(['C', 'A', 7])

question3(G) 

print "----Q3)test4----"
G=[]

question3(G)


'''
-------------------------------------Question 4
'''

# A Binary tree node

#search left tree
def left_tree(T,current_node):
    #BST have lower number on left side, Thus only search left matrix
    i = current_node
    check=True
    while check:
        i-=1
        if T[current_node][i] == 1:
            check=False
   
    return i    

#search right tree    
def right_tree(T,current_node):
    #BST have higher number on right side, Thus only search right matrix
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
    
    #error case BST should be n1 smaller than n2
    if n1>n2:
        return False

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

print ""
print "Qestion4"
print ""
 
print "----Q4)test1----" 
print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                  3,
                  1,
                  4)

print "----Q4)test2----" 
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

print "----Q4)test3----" 
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

print "----Q4)test3----" 
print question4([[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]],
                  5,
                  6,
                  1)

print "----Q4)test4----" 
print question4([[]],
                  None,
                  0,
                  0)

'''
-------------------------------------Question 5
'''

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