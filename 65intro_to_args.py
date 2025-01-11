#   * args 
# when we don't know the number of argument will be passes and we want to store them in tuple then use *
#   * operator

# def add (a,b):
#     return a+b
# print(add(3,5,6,8))     #can't do this we define funciton for two parameters and passing more than two arguments

# def add (*args):          #note args is convention we can use anything
#     print(type(args))
#     total = 0
#     for i in args:
#         total = total + i
#         # total += i 
#     return total
# print(add(3,5,6,8))

# args or any variable after * creates TUPLES of arguments 


# args with normal parameters
def multiply (num, *args):
    mul = 1
    for i in args:
        mul = mul * i
    return mul

print(multiply(0,1,2,3,4))
# so pahali argument 0 num main jayegi rest all will be in args similary jitte bhi normal parameters *args ke age honge usme pahale argument jeyege phir rest argument *args main jayege
# agar apn ne normal parameters ko *args ke bad likha then error to ayega hi kyunki sare arguments phir *args main jayege

def multiply (*args):
    print(args)
    mul = 1
    for i in args:
        mul = mul * i
    return mul

print(multiply())


#args as argument
def multiply (*args):
    # print(args)
    mul = 1
    for i in args:
        mul = mul * i
    return mul

nums = [2,3,4]
nums2 = (2,3,4,5)
print(multiply(nums))    # it will not get unpack and the list will be print 
print(multiply(*nums))    # *nums will unpack the list
print(multiply(nums2))   # tuple won't get unpack and tuple will be print
print(multiply(*nums2))    # *nums2 will unpack the tuple

# or apn direct unpack karke bhi dal sakte hian like
print(multiply(2,3,4))