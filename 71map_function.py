#map function ()
#2. The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

numbers = [1,2,3,4]
def square (num):
    return num**2


# square_list = []
# for num in numbers:
#     square_list.append(square(num))
# print(square_list)

# with map function 
#map function takes two argument pahale function and dusra iterable (string, list,etc) 
#it returns a list and hence apn for loop chala sakte hain. map object is iterator but consider it iterable for now

# square_list_2 = list(map(func, iter1))     #syntax
square_list_2 = list(map(square, numbers))
# aisa read karo square namak function main map function yek yek element of numbers ko dalega
print(square_list_2)

#apn ko function define karne ki jarurat bhi nahi hain
square_list_3 = list(map(lambda a : a**2, numbers))
print(square_list_3)

#with list comprehension
square_list_4 = [i**2 for i in numbers]
print(square_list_4)


names  = ['abc', 'abcde', 'harshit']
length = map(len, names)        #note len yek funciton pre define hain toh direct use call kar liya
for i in length:
    print(i)
# for j in length :
#     print(j)
# yek hi bar loop chala sakte ho

#abb pura list main convert ho gaya hain abb list ki properties laga sakte ho
length_2 = list(map(len, names))
for i in length_2:
    print(i)
for j in length_2:
    print(j)