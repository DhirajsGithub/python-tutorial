# generator comprehension

# square = [i**2 for i in range(1,11)]
# print(square)
# print(square)

square = (i**2 for i in range(1,11))      #it's a generator
print(square)                          # <generator object <genexpr> at 0x104ebf4a0>
# print(next(square))
# print(next(square))
# print(next(square))  #....
# # or

for num in square:
    print(num)
for num in square:
    print(num)
# yek hi bar loop chalega kyunki apne ne pahale hi square meain genrator ko generate kar diya hain

import time

# list vs generator 
#1. memory usage
#2. time

t1 = time.time()
l = [i**2 for i in range(10000000)]      
t2 = time.time()
print(t2-t1)       # 2.06 in my macky it will deffer form system to system

# almost 400mb ram used ! to store squares of 10million numbers we are not printing it caz obviosuly

t11 = time.time()
# g = (i**2 for i in range(10000000))
# negligible memory used !!!
t22 = time.time()
print(t22-t11)
# hahhahah 0.0 seconds 


# use list when you have to work with the data of the list and store in memory for functionality use
# for making to-do list we use list

