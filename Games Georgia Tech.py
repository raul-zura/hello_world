# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:50:15 2023

@author: raulz
"""

#Last problem, you wrote a function that generated the all-
#time win-loss-tie record for Georgia Tech against any other
#team.
#
#That dataset had a lot of other information in it. Let's
#use it to answer some more questions. As a reminder, the
#data will be a CSV file, meaning that each line will be a
#comma-separated list of values. Each line will describe one
#game.
#
#The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent

#This line will open the file:
record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.


#Question 1

f2 = []
for line in record_file:
    f2.append(line)

print(len(f2))
print("\n")
file = f2[1:]

print(len(file))
print("\n")

record_file.close()

d1 = []

for line in file:
    date, oponente, location, points_for, points_against = line.split(",")
        
    #print(date, oponente, location, points_for, points_against)
        
    d1.append({"date":date, "opponent":oponente, "location": location, "points for":int(points_for), "points against": int(points_against)})

#min_year = 3000
#min_month = 15
min_day= 45

#dA = []
#for date in d1:
#    dA.append(date)
#print(d1)

d2 = []
d3 = []
d4 = []

for i in d1:
    
    year, month, day = i["date"].split("-")
    
    d2.append(int(year))
    d3.append(int(month))
    d4.append(int(day))
    

min_year = min(d2)


d5 = []
for j in range(len(d1)):
    if str(min_year) in d1[j]["date"]:
       d5.append(date) 



str1 = " ".join(d5)

for j in d5:
    min_month = min(d3)
    
    if "{}-{}".format(min_year, min_month) not in str1:
        d3.remove(min_month)
    
d6 = []
for date in d5:
    if "{}-{}".format(year, month) in date:
       d6.append(date) 

str2 = " ".join(d6)

d7 = []
for date in d6:
    min_day = min(d4)
    
    if "{}-{}-{}".format(year, month, day) not in str2:
        d4.remove(min_day)
        
print("question 1")

for i in d1:
    if i["date"]== "{}-{}-{}".format(min_year, min_month, min_day):
        oponente = i["opponent"]
    
    
date = "{}-{}-{}".format(min_year, min_month, min_day)
print(date)
print(oponente)

        
#Question 2        
points_for = 0
points_against = 0

for i in d1:
    
    if i["opponent"] == "Auburn":
        #print(d1[i]["opponent"])
        
        #print(type(d1[i]["points for"]))        
        
        points_for+= i["points for"]
        
        points_against += i["points against"]

print("\nquestion 2")
print(points_for)
print(points_against)


#Question 3

wins = 0
losses = 0
ties = 0


for i in d1:
    
    if i["location"] == "Home":
        #print(i["points for"])
        
        if i["points for"] > i["points against"]:
            #print(i["points for"])
            
            wins += 1
        
        elif i["points for"] < i["points against"]:
            losses += 1
        
        else:
            ties+=1

print("\nquestion 3")
#print(len(d1))
print("{}-{}-{}".format(wins,losses,ties))

print("\nquestion 4")

wins2009 = 0
losses2009 = 0
ties2009 = 0

for i in d1:
    if "2009" in i["date"]:
        if i["points for"] > i["points against"]:
            wins2009 += 1
        elif i["points for"] < i["points against"]:
            losses2009 += 1
        else:
            ties2009 += 1

print("{}-{}-{}".format(wins2009,losses2009,ties2009))

print("\nquestion 5")

winsOctober = 0
lossesOctober = 0
tiesOctober = 0

for i in d1:
    if "-10-" in i["date"]:
        if i["points for"] > i["points against"]:
            winsOctober += 1
        elif i["points for"] < i["points against"]:
            lossesOctober += 1
        else:
            tiesOctober +=1
            
print("{}-{}-{}".format(winsOctober,lossesOctober,tiesOctober))

print("\nquestion 6")

winsSEC =0
lossesSEC = 0
tiesSEC = 0

for i in d1:
    
    year, month, day = i["date"].split("-")
    
    if int(year) in list(range(1933, 1964)):
        if i["points for"] > i["points against"]:
            winsSEC += 1
        elif i["points for"] < i["points against"]:
            lossesSEC += 1
        else:
            tiesSEC +=1
          
print("{}-{}-{}".format(winsSEC,lossesSEC,tiesSEC))


print("\nquestion 7")
dteam_points_for = {}

for i in d1:
    #print(i["opponent"])
    
    if i["opponent"] not in dteam_points_for:
        dteam_points_for[i["opponent"]] = 0
        
    dteam_points_for[i["opponent"]] += i["points for"]

#print(dteam_points_for)
maxp = 0

for k in dteam_points_for:
    
    if dteam_points_for[k] > maxp:
        maxp = dteam_points_for[k]
        team = k

print(maxp)
print(team)

print("\nquestion 8")

l = []

for k in dteam_points_for:
    
    if dteam_points_for[k] == 0:
        l.append(k)

print(l)

print("\nquestion 9")

dteam_points_against = {}

for i in d1:
    #print(i["opponent"])
    
    if i["opponent"] not in dteam_points_against:
        dteam_points_against[i["opponent"]] = 0
        
    dteam_points_against[i["opponent"]] += i["points against"]

l2 = []
    
for k in dteam_points_against:
    
    if dteam_points_against[k] == 0:
        l2.append(k)
        
print(l2)
print(len(l2))

print("\nquestion 10")

dteam_differential = {}

for i in d1:
    #print(i["opponent"])
    
    if i["opponent"] not in dteam_differential:
        dteam_differential[i["opponent"]] = 0
        
    dteam_differential[i["opponent"]] = dteam_points_for[i["opponent"]] - dteam_points_against[i["opponent"]]
    
    
maxd = 0
    
for k in dteam_differential:
    if dteam_differential[k] > maxd:
        maxd = dteam_differential[k]
        
        team_differential = k

print(maxd)
print(team_differential)


print("\nquestion 11")
number_g={}

for i in d1:
    
    
    if i["opponent"] not in number_g:
        number_g[i["opponent"]] = 0
        
    number_g[i["opponent"]] += 1

    
score_avg = {}
    
for k in number_g:
    
    if number_g[k] >=5:
    
        if k not in score_avg:
        
            score_avg[k] = 0
        
        score_avg[k] = dteam_differential[k]/number_g[k]


maxs = 0
    
for k in score_avg:
    
    if score_avg[k] > maxs:
        maxs = score_avg[k]
        
        team = k
        
print(maxs)
print(team)