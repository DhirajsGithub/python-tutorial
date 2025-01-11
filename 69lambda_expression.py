#lambda expression:
# ananomous function/ funcion without name
# def add(a,b):
#     return a+b
# print(2,3)

# with lambda expression we can write the function in one line
# lambda a,b : a+b
# above code can be read as functin do parameters lega aur return main un dono ka summation kar dega
# we can store it but it will not actually store in variable

add2 = lambda a, b : a+b
print(add2(2,3))

multiply = lambda c,d : c*d
print(multiply(2,3))

# even function
def is_even(a):
    return a%2==0
print(is_even(4))

#with lambda expression
is_even2 = lambda a : a%2 ==0
print(is_even2(7))

#last char
# last_char = lambda name : name[len(name)-1]
last_char = lambda name : name[-1]
print(last_char("harshal"))


# def func(s):
#     return len(s) > 3
#lambda with if else
func_2 = lambda s : True if len(s)>3 else False
print(func_2('abc'))