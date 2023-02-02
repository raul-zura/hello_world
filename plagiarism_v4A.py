# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 21:55:13 2023

@author: raulz
"""

import copy

def check_plagiarism(file1, file2):

    file1open = open(file1)

    text1f = file1open.read().split()
    #print(text1f)
    #print("\n")
    
    file1open.close()



    file2open = open(file2)

    text2fg = file2open.read()
    #print(text2fg)
    #print("\n")

    file2open.close()


    i = 0
    wrds = []
    phrase = []


    #for i in range(len(text1f)):
    while True:
        
        try:
            if i >0:
                if wrds:
                    wd1 = text1f[i]
                    wrds.append(wd1)
                    #i += 1
                    
                else:      
                    wrds.append(text1f[i-1])
                    wd1 = text1f[i]
                    wrds.append(wd1)
                    #i-=1
                    
            else:
                wd1 = text1f[i]
                wrds.append(wd1)
                #i += 1
                #print(wrds)
                
        except:
            break    
    
        try:
            ind = text2fg.index(" ".join(wrds))
            i+=1
            #print(wrds)
            
            if len(wrds) >= 5:
            
                #print("5", wrds)
                wrds2 = copy.deepcopy(wrds)
                
                phrase.append(wrds2)
                #print("6",phrase)
            
        except:
            #print("7", wrds)
            #i-=1
            
            if wrds:
        
                 if len(wrds) > 0:                
                     #print("1",wrds)
                     wrds.pop()
             
                     #print("2",wrds)
       
            #print("4", wrds)           
            if len(wrds) >= 5:
            
                #print("5", wrds)
                wrds2 = copy.deepcopy(wrds)
                
                phrase.append(wrds2)
                #print("6",phrase)
           
            wrds[:] = []
            
            #print("3",wrds)
            
            i+=1
            
            continue
        
        # if i>= len(text1f):
        #     break
            
    
    mx = 0
    #print("Phrase")
    #print(phrase)

    for j in range(len(phrase)):
    
        l = len(phrase[j])
    
        if l > mx:
            ind = j
            mx = l

    try:
        return " ".join(phrase[ind])
    except:
        return False


#print(check_plagiarism("text1.txt", "text2.txt"))     
print(check_plagiarism("file_ZDmWLa_v1.txt", "file_voSXqb_v1.txt"))     