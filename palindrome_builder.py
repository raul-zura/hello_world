# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 17:38:15 2023

@author: raulz
"""

#A palindrome is a sequence of letters that is the same
#forward and backward. For example, "racecar" is a
#palindrome.
#
#Write a function called create_palindrome. The function should
#have one parameter, a string. The function should return the
#string as a palindrome.
#
#If the string was not already a palindrome, the function should
#return a new string made from the original string and the
#reverse of the original string. For example:
#
# create_palindrome("abc") -> "abccba"
#
#However, if the string _is_ already a palindrome, the function
#should just return the original string by itself. For example:
#
# create_palindrome("racecar") -> "racecar"
#
#In determining whether a string is a palindrome or not, you
#should ignore punctuation, capitalization and spaces. For
#example:
#
# create_palindrome("Madam in Eden, I'm Adam") -> "Madam in Eden, I'm Adam"
#
#In creating a palindrome, though, you should use the original
#formatting:
#
# create_palindrome("Hello there!") -> "Hello there!!ereht olleH"
#
#You may assume that the only characters in the string will
#be letters, spaces, apostrophes, commas, periods, and
#question marks.
#
#Hint: Before checking if the string is a palindrome, get
#rid of the spaces and punctuation marks using the replace()
#method and convert the entire string to upper or lower
#case using the upper() or lower() methods. Remember, though,
#to keep the original string as your result should preserve
#the original punctuation and capitalization.
#
#Hint 2: There are multiple ways to do this! If you're stuck
#on one way, try a different one. You could use string
#slicing, a for loop, or some string methods. Or, try
#printing the string at different stages to see what's going
#wrong!


#Write your function here!
def create_palindrome(st):
        
    st1 = st.upper()
    
    st2 = st1
    
    for i in st:
        
        if i in " ',.?":
            st2 = st2.replace(i, "") 
    
    l = len(st2)    
    
    
    if l%2 != 0:
        mid = int((l+1)/2) - 1
        #print(mid)
        
        #print(st2[mid])
        
        left = st2[:mid]
        #print("left")
        #print(left)
        
        right = st2[mid:]
        #print("right")
        #print(right)
        
        right2 = ""
                
        
        for i in range(len(right)-1,0,-1):
            right2 += right[i]
        
        #print("Right2")
        #print(right2)
        
        if left == right2:
            return st
        else:
            st3 = ""
            
            for i in range(len(st)-1,0,-1):
                st3 += st[i]
            
            return st+st3+st[0]
        
    else:
        mid = int((l)/2) - 1
        #print(mid)
        
        #print(st2[mid])
        
        left = st2[:mid+1]
        #print("left")
        #print(left)
        
        right = st2[mid:]
        #print("right")
        #print(right)
        
        right2 = ""
                
        
        for i in range(len(right)-1,0,-1):
            right2 += right[i]
        
        #print("Right2")
        #print(right2)
        
        if left == right2:
            return st
        else:
            st3 = ""
            
            for i in range(len(st)-1,0,-1):
                st3 += st[i]
            
            return st+st3+st[0]        
        

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#racecar
#Madam in Eden, I'm Adam
#Mister in Eden, I'm EveevE m'I ,nedE ni retsiM
print(create_palindrome("racecar"))
print(create_palindrome("Madam in Eden, I'm Adam"))
print(create_palindrome("Mister in Eden, I'm Eve"))



