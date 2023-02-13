# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:49:44 2023

@author: raulz
"""

#Imagine you're writing a program to check whether sufficient
#inventory exists to fill an incoming order at a store. Your
#current inventory comes in the form of a list of instances of
#an InventoryItem class.
#
#You don't have access to the code for the InventoryItem class.
#However, you know that it has at least two attributes:
#name (a string) and quantity (an integer). The name is the
#product's name, and the quantity is the current number of that
#item that are in stock.
#
#Write a function called sufficient_inventory.
#sufficient_inventory should take three parameters: a list of
#instances of InventoryItem representing the current inventory,
#an item name (a string), and a desired quantity (an integer).
#
#The function should return True if two conditions are met:
#
# (a) There exists an instance of InventoryItem in the list
#     whose name matches the the item name parameter.
# (b) The quantity associated with that instance is larger than
#     the desired quantity.
#
#For example, imagine we called:
#
# sufficient_inventory(my_items, "hat", 3)
#
#This would return True if one of the elements in my_items had
#a name attribute "hat" and a quantity attribute greater than
#or equal to 3. It would return False if either no item in
#my_items had the name "hat", or item with the name "hat"
#has a quantity less than 3.
#
#You may assume that each item name will appear only once in
#the list of InventoryItems, and that quantity will always be
#an integer greater than or equal to 0.


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

    
def compare(lt, name, qt):
    
    oc = []
    
    for i in lt:
        #print("1")
        #print(i.name)
        #print(name)
        
        if i.name == name:        
            if i.quantity >= qt:
                return True
    
    return False
    

def sufficient_inventory(items, prod, qt):

    items = sort_std(items)
    
    prod_e = binary_search_ln(items, prod)    
    
    if prod_e:
        gqt = compare(items, prod, qt)
        
        if gqt:
            return True
        
        return False
    
    return False

#If you would like, you may implement the InventoryItem class as
#described and use it to test your code. This is not necessary
#to complete the problem, but it may help you debug. If you
#create a InventoryItem class, all you need is a constructor that
#assigns values to two attributes: self.name and self.quantity.

class InventoryItem:
    
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        
        
i1 = InventoryItem("sweater", 4)
i2 = InventoryItem("glasses", 3)
i3 = InventoryItem("sunglasses", 3)
i4 = InventoryItem("dress", 2)
i5 = InventoryItem("scarf", 5)
i6 = InventoryItem("coat", 1)
i7 = InventoryItem("skirt", 3)
i8 = InventoryItem("socks", 4)
i9 = InventoryItem("sandals", 2)

inventory = [i1, i2, i3, i4, i5, i6, i7, i8, i9]

print(sufficient_inventory(inventory, "sandals", 1))