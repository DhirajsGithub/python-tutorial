fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']
#pop method
# fruits.pop()       #it will remove last element from list by default
fruits.pop(1)        #it will remove element at indexing 1
print(fruits)

#delete keyword
del fruits[2]          #using indexing we can remove specific element indexing karni hi padegi
print(fruits)

#remove method
fruits.remove('apple')             #using element direct we can remove it
print(fruits)