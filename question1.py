# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 17:23:47 2017

@author: DUCK HA HWANG
"""

"""
Given two strings s and t, determine whether some anagram of t is a substring of s. 
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a boolean True or False.
"""

def question1(str_word, sub):
    
    if str_word.find(sub) != -1:
        return True
    elif str_word[::-1].find(sub) != -1:
        return True
    else:
        return False

    
s="udacity"
t="ad"
print question1(s,t)

s="aaaacdddity"
t="ad"
print question1(s,t)

s="Helloworld"
t="dlro"
print question1(s,t)

s="Helloworld"
t="dlrol"
print question1(s,t)