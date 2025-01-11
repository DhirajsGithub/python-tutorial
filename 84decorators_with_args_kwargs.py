# # decorators use

# from functools import wraps

# def only_int_allowed(any_function):
#     wraps(any_function)
#     def wrapper_function(*args, **kwargs):
#         data_types = []
#         for element in args:
#             data_types.append(type(element)==int)       #withuout using if statement apn yaise bhi kar sakte note: ye sirf true false hi append karega
#         if all(data_types):             #implies if all data_types are same (i.e. int here) condition will be true
#             return any_function(*args, **kwargs)
#         else:
#             print("invalid input")
    
#     return wrapper_function

# @only_int_allowed
# def add_all(*args): 
#     total = 0
#     for i in args :
#         total += i
#     return total

    


# print(add_all(1,2,3,4,9,[5,7,8,9]))     #error
# define a decorator @only int allowed to makes sure our add_all function runs 

#above code short 
# from functools import wraps
# def only_int_allowed(any_function):
#     wraps(any_function)
#     def wrapper_function(*args, **kwargs):
#         # data_type = [element for element in args if type(elment) == int] # ye jitte bhi integer hain as argument unko store karega
#         # data_types = [type(element)==int for element in args]       #ye true/ false values ko store karega
#         # if all(data_types):
#         if all([type(element)==int for element in args]):
#             return any_function(*args, **kwargs)
#         return "invalid input"
    
#     return wrapper_function


# @only_int_allowed
# def add_all (*args):
#     total = 0
#     for i in args :
#         total += i
#     return total    

# print(add_all(1,2,3,4,9,[5,7,8,9]))


# decorator with args and kwargs 
# from above example we need such decorator which will only initiate the function for specific data types

from functools import wraps
def only_data_type_allow(data_type):
    def decorator(any_func):
        @wraps(any_func)
        def wrapper(*args, **kwargs):
            data_type_check = [type(element)==data_type for element in args]
            if all(data_type_check):
                return any_func(*args, **kwargs)
            else: 
                return "invalid input"
        
        return wrapper
    return decorator             #now our main decorator is only_data_type so decorator ko bhi return karna jaruri hain




@only_data_type_allow(str)       #by passing any data type in @only_data_type_allow(datatype) below function will execute
def func_str (*args):
    string = ''
    for i in args:
        string += i
    return string

print(func_str("hars", "hal",9))