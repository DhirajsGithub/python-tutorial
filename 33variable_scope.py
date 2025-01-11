#scope 
# def func():
#     x=7
#     return x

# def func_2():
#     print(x)                  #since x is limited only in funct therfore it can't be access from func_2

# func_2()    #error


# def func():
#     x = 7    #local variable
#     return x


# print(func())      #it will print out 7 then it will show erroe for print(x)   
# print(x)                #we can't access it directly as we not call for func()


# x = 5               #global varibale
# def func():
#     x = 7
#     return x

# print(func())
# print(x)

x = 5               #global varibale
def func():
    global x                #we use global to access x directly from funct
    x = 7
    return x


print(x)                         #it will print the global variable    x=5
print(func())                     #it will call the function and print x=7
print(x)                          #since we use global x and after calling for func we print x therfore it will print x=7

