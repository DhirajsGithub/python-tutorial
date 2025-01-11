# this all are built in functions: 

# 1.enumerate function
# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.

# we use enumerate function with for loop to track position of our item in iterable 

# # with for loop 
names = ['abc', 'abcd', 'harshit']
# post = 0
# for name in names:
#     print(f"{post} -----> {name}")
#     post = post +1
#     # post += 1 
# above code without defining a varibale
# for i in range(0,len(names)):
#     print(f"{i}-----> {names[i]}")

#with enumerate function
for index, name in enumerate(names):
    print(f"{index}----->{name}")
#note pahale index dega fir element dega


#define a function taking two argument as a list and one element return where the index number in list of the argument element
# def index_pre (list, element):
#     for l in list:
#         if l == element:
#             return list.index(l)
#     return -1  
    
# print(index_pre([1,2,3,4,5], 5))

#with enumerator
def index_pre(list, element):
    for index, l in enumerate(list):
        if l == element:
            return index
    return -1
print(index_pre([1,2,3,4,5], 1))   