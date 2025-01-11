#function with all types of parameters
#very important to understand

# remember the order of parameters as PADK (param ani digvijay khairnar)

# parameters
# arg
# default parameters
# kwargs

# def func (name, *args, age = 'unknown', **kwargs ):
#     print(name)
#     print(type(name))
#     print(args)
#     print(type(args))
#     print(age)
#     print(type(age))
#     print(kwargs)
#     print(type(kwargs))

# func("Harshal", 1,2,3, a=1, b=2)

# no need to pass arguments for age as it is set default


# define a function which takes names as parameters and returns names first letter capital or reverse a name and makes first letter capital if argument followed by name is True
def func (l,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]

name = ["harshit", "mohit"]
print(func(name, reverse_str = True))

