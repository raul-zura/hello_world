# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 21:55:13 2023

@author: raulz
"""

import copy

def check_plagiarism(file1, file2):
    
    #At first I will split the first document in words
    file1open = open(file1)

    text1f = file1open.read().split()
    #print(text1f)
    #print("\n")
    
    file1open.close()


    #The second document won't be split into words
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
        
        #este bloque try-exception will verify if the while cycle has not arrived
        #to a value of greater than the number of words in the first file
        try:
            #We need to verify if the while cycle is at the beginning of the first file            
            if i >0:
                #If it is not, we need to check if there are words in the wrds list
                
                if wrds:
                    wd1 = text1f[i]
                    wrds.append(wd1)
                    #i += 1
                
                #If there are not words, these means that the program could have detected 
                #some words that appear in both documents but then it found a word that
                #was not. This word could be in both document so it is necessary to take
                #into account to make comparisons in both documents
                
                else:      
                    
                    wrds.append(text1f[i-1])
                    wd1 = text1f[i]
                    wrds.append(wd1)
                    #i-=1
                    
            else:
                #If the while cycle is at the beginning then it should only add
                #the word 
                
                wd1 = text1f[i]
                wrds.append(wd1)
                #i += 1
                #print(wrds)
        
        #If the while cycle has arrived to the end of the document, the program should
        #exit the cycle
        except:
            break    
    
        #This try-exception block evaluates if the words contained in wrds are both
        #documents. 
        try:
            #Even though we don´t use the variable ind, the try statement proves
            #if the words in the first file are in the second file
            
            ind = text2fg.index(" ".join(wrds))
            i+=1
            #print(wrds)
            
            #If the words in wrds are more than 5, then those words should be appended
            #to the phrase. This is important because if one of the documents to be
            #compared only have a set of words that are in both documents, the
            #program will return false
            if len(wrds) >= 5:
                #We have to use the deepcopy function from the copy library because 
                #it avoids that a change made to a list, member of another list 
                #happens in this second list
                
                #print("5", wrds)
                wrds2 = copy.deepcopy(wrds)
                
                phrase.append(wrds2)
                #print("6",phrase)
        
        #the except will have the following functions:
        #it will remove the last word from the wrds list because this word
        #is not included in both documents for the set of words contained in 
        #wrds. It also evaluates if wrds has more than 5 words. If it has then
        #it will add them to phrase
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

    #here we need to identify the index of phrase which corresponds to 
    #the phrase with more words
    for j in range(len(phrase)):
    
        l = len(phrase[j])
    
        if l > mx:
            ind = j
            mx = l
        
    #Here we try to join the words in the phrase with greater number of words
    #if there are no words at all, then the program should return False
    try:
        return " ".join(phrase[ind])
    except:
        return False


#print(check_plagiarism("text1.txt", "text2.txt"))     
print(check_plagiarism("file_ZDmWLa_v1.txt", "file_voSXqb_v1.txt"))     