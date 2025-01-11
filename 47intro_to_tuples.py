# tuple data structure
# tuple can store any data types 
# tuples are ordered collection of items
# most important tuples are immutable, once tuple is created you can't update it 
# we store that data inside tuple which is fixed and don't need to update
#tuples are faster than list

example = ('one', 'two', 'three')
#no append, no insert, no pop, no remove
day = ('monday', 'tuesday')
#tuples are faster than lists

# day[0] = 'sunday'
# print(day)               #error

#methods we use in tuples are
# count, index 
# len function
# slicing
#min(), max(), sum(), len()
print(example[:2])

day = ('mon', 'tue', 1, 3, ['a', 'b', 1])
print(len(day))  # 5
print(day.count(1))  # 1
print(day.index('mon'))   # 0
day_slice = day[2: 5]
print(day_slice)    # (1, 3, ['a', 'b', 1]) 

number = [3, -4, 32, -90, 0, 23]
print(min(number))   # -90
print(max(number))   # 32
print(sum(number))   # -36