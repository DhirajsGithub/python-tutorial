# intro to built in error 
# types of error :


# # syntax error
# def func:
#     pass
# func()

# name = 'Harshit'*


# # indentation error 
# def func():
#         print("hello")
#     print("hello")

# func()                                  # unindent does not match any outer indentation level


# # name error
# print(func)
# print (5+ "Harshit")                # unsopprted operand

# print(2*"harshit")                  # it will print two times harshit


# # index error

# l = [1,2,3]
# print(l[3])                         # index out of range 


# # value error 
# s = 'abc'
# print(int(s))                           # invalid literal for int() with base 10: 'abc'


# # attribute error
# l =[1,2,3,4]
# l.push(8)                                #'list' object has no attribute 'push'


# # key error
# d = {'name': 'harshit', 'hobby': 'codeinf'}
# # d['age']
# # can be avoided as
# d.get('age')                # no error



# Raise error :

def func(a,b):
    if((type(a) is int) and (type(b) is int)):
        return a+b
    # return ("OOPS! you enter a wrong error")
    raise TypeError ("OOPS! you enter a wrong error")

print(func('2', 7))