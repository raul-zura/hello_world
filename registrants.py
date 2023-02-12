# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 16:41:23 2023

@author: raulz
"""

#Imagine you're writing a program to check registration status
#at a conference. The list of registrants comes in the form of
#a list of instances of the Registrant class.
#
#You don't have access to the code for the Registrant class.
#However, you know that it has at least two attributes:
#name (a string) and authorized (a boolean).
#
#Write a function called is_authorized. is_authorized should
#take two parameters: a list of instances of Registrant
#representing the registered individuals, and a name as a
#string.
#
#The function should return True if _any_ instance in the list
#has the same name and an authorized status of True. It should
#return False if either (a) no instance in the list of
#registrants has the same name, or (b) the instance with the
#same name has an authorized status of False.
#
#You should not assume that the list of registrants is sorted
#in any way.
#
#Hint: Beware of registrants who appear in the list twice with
#different values for authorized. If _any_ instance has a
#the value True for authorized, the function should return True.


#Write your function here!



def binary_search_ln(searchList, searchTerm):
    
    name = searchTerm
    
    #searchList, d = sort_std(searchList)    
    
    #print(d)
    
    #With each recursive call to binary_search, the size
    #of the list will be cut in half, rounding down. If
    #the search term is not found, then eventually an
    #empty list will be passed into binary_search. So,
    #if searchList is empty, we know that the search
    #term was not found, and we can return False. This
    #is the base case for the recursive binary_search.

    middle = len(searchList) // 2
    
    #print(len(searchList))
    #print(searchList[middle])
    
    if len(searchList) == 0:
        return False

    #If there are still items in the list, then we want
    #to find if searchTerm is greater than, less than,
    #or equal to the middle term in the list. For that,
    #we need the index of the middle term.


    #First, the easy case: if it's the middle term, we
    #found it! Return True.
    #print(searchList[middle].last_name)
    
    if searchList[middle].name == name:
        
        return True
        
    #If the search term is less than the middle term,
    #then repeat the search on the left half of the
    #list.
    elif name < searchList[middle].name:
        return binary_search_ln(searchList[:middle], searchTerm)

    #If the search term is greater than the middle
    #term, then repeat the search on the right half
    #of the list.
    else:
        return binary_search_ln(searchList[middle + 1:], searchTerm)


def sort_std(lst):
        
    if len(lst) <= 1:
        return lst
    
    else:
        midpoint = len(lst) // 2
        
        #print(sort_std(lst[:midpoint]))
        
        left = sort_std(lst[:midpoint])
        right = sort_std(lst[midpoint:])

        newlist = []
        #newlist2 = []
        
        while len(left) > 0 and len(right) > 0:

            namel = left[0].name
            namer = right[0].name
                        
            
            if namel  < namer:
                newlist.append(left[0])
                #newlist2.append([last_namel,first_namel])
                
                del left[0]
            else:
                if namel == namer:
                    newlist.extend([left[0],right[0]])
                
                    del left[0]
                    del right[0]
                
                else:
                    newlist.append(right[0])
                    #newlist2.append([last_namer,first_namer])
                               
                    del right[0]

        newlist.extend(left)
        newlist.extend(right)
        
        #newlist2.extend(left)
        #newlist2.extend(right)

        #return newlist, newlist2
        return newlist

    
def count(lt, name):
    
    oc = []
    
    for i in lt:
        #print("1")
        #print(i.name)
        #print(name)
        
        if i.name == name:        
            oc.append(i.authorized)
    
    #print(oc)
    
    if True in oc:
        return True
    
    return False
    

def is_authorized(lt, st):
    
    lt = sort_std(lt)
    
    
    name_s = binary_search_ln(lt, st)    
    auth = False
        
    if name_s:
        
        auth = count(lt, st)
        #print(auth)        
        
    #print(name_s)
    #print(auth)
    
    if name_s and auth:
        return True
    elif not name_s or not auth:
        return False


#If you would like, you may implement the Registrant class as
#described and use it to test your code. This is not necessary
#to complete the problem, but it may help you debug. If you
#create a Registrant class, all you need is a constructor that
#assigns values to two attributes: self.name and self.authorized.

class Registrant:
    
    def __init__(self, name, authorized):
        self.name = name
        self.authorized = authorized
        
#p1 = Registrant("Rayan Sparks", True)
#p2 = Registrant("Rayan Sparks", True)
#p3 = Registrant("Rayan Sparks", False)
#p4 = Registrant("Holden Bullock", False)
#p5 = Registrant("Holden Bullock", False)
#p6 = Registrant("Braylen Richard", False)
#p7 = Registrant("Lucy Moran", True)
#p8 = Registrant("Ping Moran", False)    
#p9 = Registrant("Braylen Scott", True)

#lt = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

#print(is_authorized(lt, "Barbara Pittman"))
        
p1 = Registrant("Taryn Foley", False)
p2 = Registrant("Taryn Foley", True)
p3 = Registrant("Taryn Elliot", True)
p4 = Registrant("Vaughn Roberson", True)
p5 = Registrant("Vaughn Richard", False)
p6 = Registrant("Kelly Roberson", False)

lt = [p1, p2, p3, p4, p5, p6]

print(is_authorized(lt, "Taryn Foley"))