# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 18:12:29 2017

@author: DUCK HA HWANG
"""

"""
Question 2

Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string.
"""

def question_2(s):
    """
    :type s: str
    :rtype: str
    """
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

a="babad"
print question_2(a)

a="cbbd"
print question_2(a)

a="budaaduudaaduc"
print question_2(a)

a="cbbdbabadaaccccawreeeeeeeeeebdbdbdbbddbbcbadsadwqeo"
print question_2(a)