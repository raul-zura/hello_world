# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 12:05:01 2023

@author: raulz
"""

#Imagine you're writing a program to check attendance on a
#classroom roster. The list of students in attendance comes
#in the form of a list of instances of the Student class.
#
#You don't have access to the code for the Student class.
#However, you know that it has at least two attributes:
#first_name and last_name.
#
#Write a function called check_attendance. check_attendance
#should take three parameters: a list of instances of
#Student representing the students in attendance, a first
#name as a string, and a last name as a string (in that
#order).
#
#The function should return True if any instance in the
#list has the same first and last name as the two
#arguments. It should return False otherwise.
#
#You may assume that the list of students is sorted
#alphabetically, by last name and then by first name. This
#allows you to solve this with a binary search. However,
#you may also solve this problem with a linear search if
#you would prefer.


#Write your function here!


def binary_search_ln(searchList, searchTerm):
    
    fn, ln = searchTerm
    
    #searchList, d = sort_std(searchList)    
    
    #print(d)
    
    #With each recursive call to binary_search, the size
    #of the list will be cut in half, rounding down. If
    #the search term is not found, then eventually an
    #empty list will be passed into binary_search. So,
    #if searchList is empty, we know that the search
    #term was not found, and we can return False. This
    #is the base case for the recursive binary_search.

    if len(searchList) == 0:
        return False

    #If there are still items in the list, then we want
    #to find if searchTerm is greater than, less than,
    #or equal to the middle term in the list. For that,
    #we need the index of the middle term.

    middle = len(searchList) // 2

    #First, the easy case: if it's the middle term, we
    #found it! Return True.
    #print(searchList[middle].last_name)
    
    if searchList[middle].last_name == ln:
        
        if searchList[middle].first_name == fn:
            return True
        
        elif fn < searchList[middle].first_name:
            return binary_search_ln(searchList[:middle], searchTerm)
        
        else:
            return binary_search_ln(searchList[middle + 1:], searchTerm)
        
    #If the search term is less than the middle term,
    #then repeat the search on the left half of the
    #list.
    elif ln < searchList[middle].last_name:
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

            last_namel = left[0].last_name
            first_namel = left[0].first_name
            
            last_namer = right[0].last_name
            first_namer = right[0].first_name
            
            if last_namel  < last_namer:
                newlist.append(left[0])
                #newlist2.append([last_namel,first_namel])
                
                del left[0]
            else:
                if left[0].last_name == right[0].last_name:
                    if left[0].first_name < right[0].first_name:
                        newlist.extend([left[0], right[0]])
                        #newlist2.extend([[last_namel, first_namel],[last_namer, first_namer]])                              
                               
                    else:
                        newlist.extend([right[0], left[0]])
                        #newlist2.extend([[last_namer, first_namer],[last_namel, first_namel]])
                                        
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

    
def binary_search2(searchList, searchTerm):
    
    fn, ln = searchTerm
    
    #searchList, d = sort_std(searchList)    
    
    print("\nordered list binary_search2")
    print(searchList)
    print("\n")
    
    #With each recursive call to binary_search, the size
    #of the list will be cut in half, rounding down. If
    #the search term is not found, then eventually an
    #empty list will be passed into binary_search. So,
    #if searchList is empty, we know that the search
    #term was not found, and we can return False. This
    #is the base case for the recursive binary_search.

    if len(searchList) == 0:
        return False

    #If there are still items in the list, then we want
    #to find if searchTerm is greater than, less than,
    #or equal to the middle term in the list. For that,
    #we need the index of the middle term.

    middle = len(searchList) // 2

    #First, the easy case: if it's the middle term, we
    #found it! Return True.
    #print(searchList[middle].last_name)
    
    slln = searchList[middle][0]
    slfn = searchList[middle][1]
    #print(slln, slfn)
    #print(ln, fn)
    
    if slln == ln:
        #print("yeah")
        #print(ln)
        
        #print("yeah2")
        #print(slfn, fn)
        
        if slfn == fn:
            return True
        
        elif fn < slfn:
            return binary_search2(searchList[:middle], searchTerm)
        
        else:
            return binary_search2(searchList[middle + 1:], searchTerm)
        
    #If the search term is less than the middle term,
    #then repeat the search on the left half of the
    #list.
    elif ln < slln:
        return binary_search2(searchList[:middle], searchTerm)

    #If the search term is greater than the middle
    #term, then repeat the search on the right half
    #of the list.
    else:
        return binary_search2(searchList[middle + 1:], searchTerm)


def sort_std2(lst):
        
    if len(lst) <= 1:
        return lst
    
    else:
        midpoint = len(lst) // 2
        
        print("1")
        print(sort_std2(lst[:midpoint]))
        print("2")
        
        print("left")
        left = sort_std2(lst[:midpoint])
        print(left)
        
        print("right")
        right = sort_std2(lst[midpoint:])
        print(right)
        
        newlist = []
        #newlist2 = []
        
        while len(left) > 0 and len(right) > 0:

            last_namel = left[0][0]
            first_namel = left[0][1]
            print("left n and f")
            print(last_namel, first_namel)
            
            last_namer = right[0][0]
            first_namer = right[0][1]
            print("right n and f")
            print(last_namer, first_namer)            
            
            if last_namel  < last_namer:                
                newlist.append([last_namel,first_namel])
                
                del left[0]
            else:
                if last_namel == last_namer:
                    if first_namel < first_namer:    
                        print("\n")                      
                        newlist.extend([[last_namel, first_namel],[last_namer, first_namer]])                              
                        print(newlist)
                        print("hey")
                               
                    else:           
                        print("\n")
                        newlist.extend([[last_namer, first_namer],[last_namel, first_namel]])
                        print(newlist)
                        print("hey2")
                                        
                    del left[0]
                    del right[0]
                
                else:                    
                    newlist.append([last_namer,first_namer])
                               
                    del right[0]

        newlist.extend(left)
        newlist.extend(right)
        
        #newlist2.extend(left)
        #newlist2.extend(right)

        #return newlist, newlist2
        return newlist    

    
def lt_ln(lt):
    
    lt2 = []

    for i in lt:
        fn = i[0]
        ln = i[1]
        
        lt2.append([ln,fn])
        
    return lt2

            
def check_attendance(lt, fn, ln):
    searcht = [fn, ln]        
    
    lt = sort_std(lt)
    
    st=binary_search_ln(lt, searcht)
    #print(st)
    
    return st


def check_attendance2(lt, fn, ln):
    searcht = [fn, ln]
    
    lt = lt_ln(lt)
    
    lt = sort_std2(lt)
    
    print("catt")
    print(lt)
    
    
    
    st=binary_search2(lt, searcht)
    #print(st)
    
    return st
    
#If you would like, you may implement the Student class as
#described and use it to test your code. This is not
#necessary to complete the problem, but it may help you
#debug. If you create a Student class, all you need is
#a constructor that assigns values to two attributes:
#self.first_name and self.last_name.

class Student:
    
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        
#std1 = Student("Marguerite", "Arnold")
#std2 = Student("Kamari", "Roberson")
#std3 = Student("Joshua", "Velazquez")
#std4 = Student("Joshua", "Macdonald")
#std5 = Student("Jackie", "Velazquez")

#lt = [std1, std2, std3, std4, std5]
#lt = [std1,std4,std2,std5,std3]

#print(check_attendance(lt, "Joshua", "Macdonald"))
#print("\n")
          
                                        
#std1 = Student("Rayan", "Wong")
#std2 = Student("Rayan", "Mccarty")
#std3 = Student("Lindsay", "Wong")
#std4 = Student("Haylee", "Sparks")
#std5 = Student("Saniya", "Roberson")
#std6 = Student("Ashtyn", "Roberson")
#std7 = Student("Gautam", "Foley")
#std8 = Student("Gautam", "Simpson")                                        
#lt = [std1, std2, std3, std4, std5, std6, std7, std8]

#print(check_attendance(lt, "Kamari", "Roberson"))
#print("\n")                                  


#std1 = Student("Barbara", "Bullock")
#std2 = Student("Barbara", "Velazquez")
#std3 = Student("Joshua", "Velazquez")
#std4 = Student("Joshua", "Pittman")
#std5 = Student("Yadira", "Murrell")
#std6 = Student("Madisyn", "Morales")
#std7 = Student("Madisyn", "Velazquez")                         

#lt = [std1, std2, std3, std4, std5, std6, std7]
#lt = [std1,std4,std2,std5,std3]

#print(check_attendance(lt, "Madisyn", "Velazquez"))
#print("\n")                                  

#lt = [["Barbara","Bullock"],["Barbara","Velazquez"],["Joshua","Velazquez"],["Joshua","Pittman"],["Yadira","Murrell"],["Madisyn","Morales"],["Madisyn","Velazquez"]]

#print(check_attendance2(lt, "Madisyn", "Velazquez"))

std1 = Student("Rayan", "Elliott")
std2 = Student("Rayan", "Barker")
std3 = Student("Rayan", "Simpson")
std4 = Student("Gilbert", "Simpson")
std5 = Student("David", "Simpson")
std6 = Student("Kelly", "Velazquez")
std7 = Student("Haylee", "Simpson")
std8 = Student("Lindsay", "Moran")
std9 = Student("Lindsay", "Morales")

lt = [std1, std2, std3, std4, std5, std6, std7, std8, std9]

print(check_attendance(lt, "Rayan", "Simpson"))
print("\n")                                  



#lt = [["Rayan","Elliot"],["Rayan","Barker"],["Rayan","Simpson"],["Gilbert","Simpson"],["David","Simpson"],["Kelly","Velazquez"],["Haylee","Simpson"],["Lindsay","Moran"],["Lindsay","Morales"]]

#print(check_attendance2(lt, "Rayan", "Simpson"))