# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 15:05:11 2023

@author: raulz
"""

#-----------------------------------------------------------
#The United States Social Security Administration publishes
#a list of all documented baby names each year, along with
#how often each name was used for boys and for girls. The
#list is used to see what names are most common in a given
#year.
#
#We've grabbed that data for any name used more than 25
#times, and provided it to you in a file called
#babynames.csv. The line below will open the file:

names_file = open('../resource/lib/public/babynames.csv', 'r')

#We've also provided a sample subset of the data in
#sample.csv.
#
#Each line of the file has three values, separated by
#commas. The first value is the name; the second value is
#the number of times the name was given in the 2010s (so
#far); and the third value is whether that count
#corresponds to girls or boys. Note that if a name is
#given to both girls and boys, it is listed twice: for
#example, so far in the 2010s, the name Jamie has been
#given to 611 boys and 1545 girls.
#
#Use this dataset to answer the questions below.


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.


#Question 1
f = []

for line in names_file:
    f.append(line.strip().split(","))

names_file.close()
#print(f)

f2 = f[:]

f2.sort(key=lambda x: x[0])


#print(f2)
print(len(f2))

names = []

for i in f2:
    name = i[0]
    
    if name not in names:
        names.append(name)

print("Question 1")
print(len(names))


#Question 2

names_count = 0
    
for i in f2:
    
    name_count = int(i[1])
    
    names_count += name_count
 
print("Question 2")
print(names_count)


#Question 3
z_count =0

for i in f2:
    name = i[0]
    #print(name)
    #print(i[2])
    
    if i[2] == "Boy":
        
        if "Z" == name[0]:
            #print(name)
            #print(i[2])

            
            z_count += 1

print("Question 3")
print(z_count)


#Question 4

maxn = 0
    
for i in f2:
    name = i[0]
    
    num = int(i[1])
    
    if i[2] == "Girl":
        
        if "Q" == name[0]:
            if num > maxn:
                maxn = num
                nameq = name

print("Question 4")
print(nameq)
      
#Question 5
      
count = 0
      
for i in f2:
    name = i[0]
    count_d = int(i[1])
    
    #print(name)
    #print(name[0])
    #print(name[-1])
      
    if name[0] in "AEIOUaeiou" and name[-1] in "AEIOUaeiou":
        count += count_d

print("Question 5")
print(count)


#Question 6

dletter = {}

for i in f2:
    
    name = i[0]
    iname = name[0]
    count = int(i[1])
    
    if iname not in dletter:
        dletter[iname] = 0
        
    dletter[iname] += count
    
key_letter = min(dletter, key = dletter.get)

print("Question 6")
print(key_letter)
print(dletter[key_letter])

#Question 7
count_lc=0

for i in f2:
    
    name = i[0]
    numb = int(i[1])
    
    if name[0] == "U":
        count_lc += numb
        
print("Question 7")
print(count_lc)

#Question 8

key_letter = max(dletter, key = dletter.get)

print("Question 8")
print(key_letter)

print("Question 9")
print(dletter[key_letter])


#Question 10

namd = {}

for i in f2:
    name = i[0]
    count = int(i[1])
    
    if name not in namd:
        namd[name] =0
        
    namd[name] += count

print("Question 10")
#print(f2)
key_name = max(namd, key = namd.get)

print(key_name)

print(namd["Jamie"])

print("Question 11")
print(namd[key_name])

#print(f2.index("Sophia"))

#Question 12
name_g = {}

for i in f2:
    name = i[0]
    count = int(i[1])
    gender = i[2]
    
    if name not in name_g:
        name_g[name] = [0,0]
    
    if gender == "Girl":
        name_g[name][0] += count
    else:
        name_g[name][1] += count

dif_d = {} 

for i in name_g:
    girl_count = name_g[i][0]
    boy_count = name_g[i][1]
    
    if boy_count != 0 and girl_count != 0:
        if i not in dif_d:
            dif_d[i] = 0
        
        dif_d[i] = abs(girl_count - boy_count)
    
key_name = min(dif_d, key = dif_d.get)
print("Question 12")
print(key_name)
print(dif_d["Keylen"])
#print(dif_d)

difl = []

for i in dif_d:
    difl.append([i, dif_d[i]])

print("hum")
#print(difl)

from operator import itemgetter
difl.sort(key= itemgetter(1))

print(difl)