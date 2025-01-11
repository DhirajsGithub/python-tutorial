fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

#1.count() method
print(fruits.count('apple'))         #it will count specific element
print(len(fruits))

#2.sort() method rearrange elements in ascending order
fruits.sort()               #isne fruits ko affect kar dala
print(fruits)

numbers = [3, 5, 1, 9, 10, -2, -9]
print(sorted(numbers))                    #note it will only print sorted numbers it won't affect numbers list

# #3.clear() method
# numbers.clear()
# print(numbers)

#4.copy() method
# numbers_copy = numbers.copy()
# print(numbers_copy)

#5.reversing a list
numbers.reverse()
print(numbers)

#6. index() method
index_of = numbers.index(5, 0, len(numbers))   #  numbers.index(what_to_find, where to start, where to end)
print(index_of)


# min, max