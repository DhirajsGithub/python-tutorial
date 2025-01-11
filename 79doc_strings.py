# doc strings
# help us what the function is for

def add_two(a,b):
    '''this function takes two numbers and return their sum'''
    return a+b
print(add_two(2,3))
print(add_two.__doc__)

# some in-built funciton like len, sum, min/max, sorted, etc
print(len.__doc__)
print(sorted.__doc__)
# very useful 

print(help(sorted))
# in this way we can access what are in-built function are built for

