# Decorators - enhance the functionality of other functions  

def decorator_function(any_function):
    def wrapper_function():
        print("this is awesome function")
        any_function()
    return wrapper_function



@decorator_function     #shortcut  jis function per apply karn hain usi ke upar likhna jaruri hain
def func_1():
    print("this is function 1")

def func_2():
    print("this is function 2")

# we want to add more to the above functions without changing the original functions so make a decorator function

# M-1
var = decorator_function(func_1)             
var()                                                 #wrapper function any_fucntion ko bhi call kar raha hain toh agar wrapper fucntion ko call kiya toh any_funct bhi call ho jayega
# or we can also give var name of func
func_2 = decorator_function(func_2)          
func_2()

# M-2
func_1()                        # @decorator_function will take care of calling decoreator_function and passing any function to it


# problem #1 no parameter in wrapper function and hence we can't give arguments to func_1 
# TypeError: wrapper_function_1() takes 0 positional arguments but 1 was given
# solutio @prob-1 : hence wraper function and any_function  main *args or **kwargs or both as parameters likhna jaruri hain

# problem #2 we only call our any_function .| solution @ prob-2 : hence we should return it

# problem #3 docstring problem if we add docstring to any function it will print doc string of wrapper function hence import wraps and use it for any_function

from functools import wraps 

def decorator_function_1(any_function_1):
    @wraps(any_function_1)
    def wrapper_function_1(*args, **kwargs):                 # for arguments from add/ func_11
        print(f"you passes {args} in {any_function_1.__name__}")
        '''this is docstring of wrapper function_1 '''
        print("decorator function is called")
        return any_function_1(*args, **kwargs)
    return wrapper_function_1


@decorator_function_1
def func_11(a):
    print(f"this is function 11 with argument {a}")

func_11(4)

# wrapper funtion also takes (4)

var = decorator_function(func_11)
var(5)


@decorator_function_1
def add(a,b):
    '''this is docstring of add function'''
    return a+b
print(add(2,3))

print(add.__doc__)
print(add.__name__)



# Q.
# output of function add_func be like
# your are calling add_func function
# This function takes two numbers as parameters and returns their sum
# 9

from functools import wraps 
def print_function_data(function):
    @wraps(function)
    def wrapper_function_11(*args, **kwargs):
        print("you are calling for {}".format(function.__name__))
        print(function.__doc__)
        return function(*args, **kwargs)
    return wrapper_function_11

@print_function_data
def add_func(a,b):
    '''this function takes two numbers as parameters and returns their sum'''
    return a+b
print(add_func(5,4))
# output of function add_func be like
# your are calling add_func function
# This function takes two numbers as parameters and returns their sum
# 9


# make a decorator and find time taken to complete the task

from functools import wraps
 
import time

def decorator_cal_time(function):
    @wraps(function)
    def wrapper_func(*args, **kwargs):                
        print(f"decorator call{function.__name__}")
        t1 = time.time()
        returned = function(*args, **kwargs)
        t2 = time.time()
        print(f"this function took {t2-t1} seconds")
        return returned       #direct return nahi kiya kyunki execution direct return ke bad uss loop se jump kar jayegi hence t2 calculate nahi kar payenge 
    return wrapper_func



@decorator_cal_time
def func_time(n):
    return [i**10 for i in range(1,n+1)]

func_time(100)
