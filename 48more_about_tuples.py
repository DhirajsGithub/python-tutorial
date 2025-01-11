# #looping in tuples:
# import re
# from typing_extensions import runtime


# mixed = (1,2,4,6,0)
# #for loop in tuples:
# for element in mixed:
#     print(element)
    

# #tuple with one element
# nums = (1)
# print(type(nums))         #it will obviously show int as a class
# number = (1,)
# print(type(number))           #<class 'tuple'>
# #so kya sikhe yek hi element ka tuple banana ho toh yek comma lagana jaruri hain
# words = ('word1',)
# print(type(words))


# #tuple without parenthesis
# guitars = 'yamaha','baton rouge', 'taylor'
# print(type(guitars))          # it will print tuple as class 


# #list inside tuples
# series = ('money heist',['mirzapur', '13-reasons why', 'squid games'])
# print(series[1])
# series[1].pop()
# print(series)
# series[1].append('gans of wasipur')
# print(series) 
# #so we can do all thing with list inside list of tuples


# #some function in tuples
# numbers = (1,5,7,8)
# print(min(numbers))
# print(max(numbers))

# print(sum(numbers))           # note the syntax to print the summation 

print('------tuples unpackig------------')
# tuples unpacking 
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits
(green, *red, yellow) = fruits        # don't take is as *args or **kwargs
# NOTE: '*' is known as asterisk ---> which means remaining unoccupied values will be assign to that vairbale. 
# asterisk will store remaining values in list.  

print(green)
print(red)
print(yellow)
print(fruits*2)