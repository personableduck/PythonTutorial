# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 12:32:33 2017

@author: 1234
"""

 
# The main function
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

print '----test 1----'

G=[]
G.append(['a', 'b', 10])
G.append(['a', 'c', 6])
G.append(['a', 'd', 5])
G.append(['b', 'd', 15])
G.append(['c', 'd', 4])  
            
question3(G)

print '----test 2----'

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
        
print '----test 3----'    

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