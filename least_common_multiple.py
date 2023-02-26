# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 12:41:50 2023

@author: raulz
"""

def find_lcm(fn, sn):
    
    return int(fn*sn/(find_gcf(fn, sn)))


def find_gcf(numb1, numb2):
    
    b = min([numb1, numb2])    
    a = numb1 + numb2 -b    
    
    while b!=0:                    
        
        temp = b
        b = a % b    
        #print("this is b")
        #print(b)
        
        a = temp        

        #print(a, b)                
    
    return a

print(find_lcm(2, 10))
print(find_lcm(2, 7))
print(find_lcm(4, 6))
print(find_lcm(5, 5))