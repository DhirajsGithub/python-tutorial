#defining a function which gives bigger of two number
def is_bigger (a,b):
    if a>b :
        return a
    return b

# print(is_bigger(5,9))

#define a function which tells bigger of three numbers
#so we take helf of above function to make such function

# def is_greatest (a,b,c):
#     greater = (is_bigger(a,b))
#     return is_bigger(greater,c)

# print(is_greatest(5,9,1))

def is_greatest (a,b,c):  
    return is_bigger((is_bigger(a,b)),c)

print(is_greatest(5,9,1))


# recursion
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is the process of determining something in terms of itself

# calculate a factorial of a number using recursion function 
def fact (n):
    if n == 1:
        return 1
    else :
        return n * fact(n-1)
    
print(fact(8))

# 1. fact(5): returns 5 * fact(4)
# 2. fact(4): retutns 4 * fact(3)
# 3. ....
# 4. fact(1) : returns 1 and hence the block termiates

# how to stop recursive function 
# there has to be a base limit in each recursive program, or the program will run infinitely 
import re
import sys
print(sys.getrecursionlimit())            # 1000

# recurive funtion can be hard to deefine, recursive calls are expensive as they take lot of memory and space hard to debug
# But code is clean and elegant in recursive funtion, a composite task can be broken down into simpler sub-problems using recursion
# generating sequence is easier with recursion than using nested loop

def summtn(n):
    if n ==1 :
        return 1
    else : 
        return (n + summtn(n-1))
    
print(summtn(5))


# funtion returning reverse of a string

def funt(s):
    if len(s) >=1:
        return (s[len(s)-1]) + funt(s[0:len(s)-1])
    else :
        return ""



print(funt("anurag"))


# Write a recursive function that takes a list of numbers as an input and returns the product of all the numbers in the list.

def all_pro(l):
    if len(l) >=1:
        return l[0] * all_pro(l[1:]) 
    else:
        return 1
print(all_pro([1,2,3,4,5]))

# Write a function that takes a string and returns if the string is a palindrome.
def isPalindrom(strng):
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng)-1]:
        return False
    return isPalindrom(strng[1:-1])


# Write a recursive function that takes an array that may contain more arrays in it and returns an array with all values flattened
def flat(l):
    x = []
    for i in l:
        if type(i) is list:
            x.extend(flat(i))
        else :
            x.append(i)
    return x

# Write a recursive function that takes an array of words and returns an array that contains all the words capitalized.

