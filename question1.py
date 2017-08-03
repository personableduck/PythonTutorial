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