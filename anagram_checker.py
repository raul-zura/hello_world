# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:18:14 2023

@author: raulz
"""

#Write a function called are_anagrams. The function should
#have two parameters, a pair of strings. The function should
#return True if the strings are anagrams of one another,
#False if they are not.
#
#Two strings are considered anagrams if they have only the
#same letters, as well as the same count of each letter. For
#this problem, you should ignore spaces and capitalization.
#
#So, for us: "Elvis" and "Lives" would be considered
#anagrams. So would "Eleven plus two" and "Twelve plus one".
#
#Note that if one string can be made only out of the letters
#of another, but with duplicates, we do NOT consider them
#anagrams. For example, "Elvis" and "Live Viles" would not
#be anagrams.


#Write your function here!
def are_anagrams(st1, st2):
    
    st1A = st1.lower()
    st2A = st2.lower()
    
    chars = ",.-?! "
    
    st1B=st1A
    
    for i in st1A:
        if i in chars:
            st1B = st1A.replace(i,"")
    
    st2B = st2A
    
    for i in st2B:
        if i in chars:
            st2B =st2A.replace(i,"")
    
    #print("strings")
    #print(st1B)
    #print(st2B)
    
    dt1 = {}
    
    for i in st1B:
        
        if i not in dt1:
            dt1[i] = 0
        
        dt1[i] += 1
        
    
    dt2 = {}
    
    for i in st2B:
        
        if i not in dt2:
            dt2[i] =0
        
        dt2[i] += 1
        
    
    k1 = list(dt1.keys())
    #print(k1)
    k1.sort()
    
    k2 = list(dt2.keys())
    k2.sort()
    
    #print("k1, k2")
    #print(k1, k2)
    
    if k1 == k2:
        
        for i in k1:
            if dt1[i] != dt2[i]:
                return False
    else:
        return False
    
    return True

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, True, False, each on their own line.
print(are_anagrams("Elvis", "Lives"))
print(are_anagrams("Elvis", "Live Viles"))
print(are_anagrams("Eleven plus two", "Twelve plus one"))
print(are_anagrams("Nine minus seven", "Five minus three"))


