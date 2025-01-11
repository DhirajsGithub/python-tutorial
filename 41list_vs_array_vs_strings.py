#list vs array
#both are order collectin of items

# Arrays need to be declared. Lists don't

#c, c++, java   have array
#can store only one type of data

#list in pyhon can store any type of data
#list are flexible
#javascript have array which is as flexible as list
 
#python too have array module which store fix data type having high performance but we don't use them caz
#when we do calculation in data science we use numpy array and numpy arrays binding is with c
#numpy arrays have more speed as like c

#numpy array - binding with c libraries

#list vs strings
#strings are immutable
#lists are mutable

s = "string"
s.title()               #apn direct original string main change nahi kar sakte
print(s)
t = s.title()          #it will make change in s and store in t
print(t)

l = ['world1', 'world2', 'world3']
l.append("word4")                       #apn original list main direct change kar sakte hain
print(l)