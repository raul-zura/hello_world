# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:24:56 2023

@author: raulz
"""

def deobfuscate(output_file, input_file):
    
    out = open(output_file, "w")
    inp = open(input_file, "r")
    
    stp = ""
    
    for c in inp:
        stp += c
        
    inp.close()
    
    st = ""
    
    for i in range(len(stp)):
        
        ind = i +1
        
        if ind%2==0:
            st+= stp[i]+stp[i-1]
            
    if len(stp)%2!=0:
        st+= stp[-1]

    print(st, file = out, end="")
    