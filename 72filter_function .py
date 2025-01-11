#3.filter function ()
#The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

def is_even (a):
    return a%2==0

numbers = [1,2,3,4,5,6,7,8,9]
 
#to sort out all the evens we have filter function
# evens = list(filter(function, iterable))  #syntax 

# evens = tuple(filter(is_even, numbers))
evens = list(filter(is_even, numbers))
print(evens)

#without initially defining a function
evens_2 = list(filter(lambda a : a%2 ==0 , numbers))
print(evens_2)

#with list comprhension
evens_3 = [a for a in numbers if a%2 ==0 ]
print(evens_3)          
