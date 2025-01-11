# generators 
# generators are iterators like
# iterators and iterable are differ 
# consider like iterators are subset of iterable 

l = [1,2,3,4,5]    #iterable
i = iter(l)         #iterator

# for num in l :
#     print(num)
# this for loop runs in form of iterator to execute the iterable

# for loop hame ye kaam kareke deta hain upto length of iterable
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# # print(next(i))     # error StopIteration

# print(next(l))       # error list' object is not an iterator since l is iterable

square = map(lambda a : a**2 , l)        # iterator
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))

# or 
# for s in square :
#     print(s)

# note iterator ke case main apn sirf yek hi bar loop chala sakte hain
# but we can convert iterator to iterable 
square_l = list(square)       # iterable
print(type(square_l))

# in terms of list
# memory ---->  [...........................]   stores all the data wheter we are dealing with one or two memory will store all data of lists

# in terms of generators 
# memory ---->  [...]   jitna data chahihye memory utna hi store karegi

# note : we use generator jab hame itarable ko sirf yek hi time use karna hota hain
# benefits of generator : less usage of memory, saving time


# create your first generator :
# 1.) generator function

# def func (n):
#     for i in range(1,n+1):
#         print(i)
# noraml function which prints/ returns

# that's our generator function
def func (n):
    for i in range(1,n+1):
        yield i
        # yield (i)

print(func(10))        # <generator object func at 0x102ff36d0>
numbers = func(10)
for num in numbers :
    print(num)
for num in numbers :
    print(num)
# since it's generator function and hence the loop won't work multiple time 

print("-------------------")

# define a genearator taking any number as argument and returning even numbers upto that numbers

def is_even(n):
    for num in range(1,n+1):
        if num%2==0:
            yield num

even_generate = is_even(8)
for i in even_generate :
    print(i)

print("-------------------")

# note : apn ne genrate kar liya uske bad apn for loop dubara nahi chala sakte(line 65, 67)  here even_generate main apn ne generate kar liya toh bad main phir se for loop nahi chala sakte
# lekin agar apn bar bar generate kara rahe(line 89, 91, 93) he aur uspe for loop bar bar laga rahe hain toh for loop chalegi bar bar

for j in is_even(4):
    print(j)
for j in is_even(4):
    print(j)
for j in is_even(4):
    print(j)