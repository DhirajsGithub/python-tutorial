#iterables vs iterate

numbers = [1,2,3,4]  #iterables   Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:

square = map(lambda a: a**2 , numbers)   #iterator since map functioni stores in iterator

# for i in numbers:
#     print(i)

# step-1 call iter functin
# step-2 apply next to all the iter funcitons 

#for iterable 
# print(next(numbers))       #error
number_iter = iter(numbers)      #iterable ko iterate main convert kiya
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
# print(next(number_iter))       #error  StopIteration
# one by one element are iterate from numbers 

#for iterate
print(next(square))
print(next(square))
print(next(square))