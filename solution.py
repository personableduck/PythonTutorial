# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 17:40:04 2017

@author: DUCK HA HWANG
"""

#-------------------------------------Question 1

def question1(str_word, sub):
    
    if str_word == "" or sub == "":
        return False
    
    if str_word.find(sub) != -1:
        return True
    elif str_word[::-1].find(sub) != -1:
        return True
    else:
        return False

print "Qestion1"
print ""
print "----Q1)test1----"      
s="udacity"
t="ad"
print question1(s,t)

print "----Q1)test2----"  
s=""
t="ad"
print question1(s,t)

print "----Q1)test3----"  
s="Helloworld"
t="dlro"
print question1(s,t)

print "----Q1)test4----"  
s="Helloworld"
t=""
print question1(s,t)

#-------------------------------------Question 2

def question_2(s):
    """
    :type s: str
    :rtype: str
    """
#==============================================================================
#     if s == "":
#         return ""
#==============================================================================
    
    ss=s[::-1]
    rtype=[]
    length_value_fix=len(s)
    
    for index in range (length_value_fix):
        
        finding=s[index]    
        check_max=len(rtype)
        pass_flag=s[index+check_max:].find(finding)
        
        if pass_flag != -1:
        
            while ss:      
                reversed_location=ss.find(finding)
                s_recall=ss[reversed_location:]
                s_reversed=s_recall[::-1]      
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

#-------------------------------------Question 3

def question3(G):
    
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

#-------------------------------------Question 4

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
     
    # Base Case
    if r is None:
        return None
    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(r > n1 and r > n2):
        return question4(T,left_tree(T,r), n1, n2)
 
    # If both n1 and n2 are greater than root, then LCA
    # lies in right 
    if(r < n1 and r < n2):
        return question4(T,right_tree(T,r), n1, n2)
 
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
                  6,
                  1)

print "----Q4)test4----" 
print question4([[]],
                  None,
                  0,
                  0)

#-------------------------------------Question 5

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def question5(first_node,end_search):
    data_storage=[]
    readNode(node1,data_storage)
    
    if len(data_storage) - end_search < 0:
        return False
    
    return data_storage[len(data_storage) - end_search]
    
def readNode(node,data_storage):
    data_storage.append(node.data)
    if node.next != None:
        readNode(node.next,data_storage)

print ""
print "Qestion5"
print ""
    
print "----Q5)test1----"

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

print "----Q5)test2----" 

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

print "----Q5)test3----"  

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

print "----Q5)test4----"  

node1 = Node(5)

print question5(node1, 4)