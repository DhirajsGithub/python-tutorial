# 
#note: else statement yakeli nahi ho sakti

# The number of spaces is up to you as a programmer, but it has
# to be at least one. 

#if elif else statement 
# show ticket pricing 
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)
# age = int (input("enter your age"))

# if 1<=age<=3:
#     print("free")
# elif 4<=age<=10:
#     print("150")
# elif 11<=age<=60:
#     print("250")
# elif age>=60:
#     print("200")
# else :
#     print("invalid")


# # in_keyword
# # if with in:

from queue import PriorityQueue


name = "Harshit"
if "H" in name:
    print("H is presesnt in name")
else :
    print("H is not present in name")

# if with not in:
if "d" not in name:
    print("d is not in {}".format(name))
else:
    print(f"d is in {name}")


#check empty or not
name = input("enter your name ")

if name :                                               # if name true hain toh hain condition true hogi aur if wali statement chalegi
    print(f"your name is {name}")
else: 
    print("you didn\'t type anything")


# short hand if/ if else statement 
a = 3
b = 2
if a > b : print("hellow")

print("Hellow") if a > b else print("Land")