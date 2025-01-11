# make a function divide
# which will handle the errors like

# try:
#     num1= int(input("enter a number : "))
#     num2 = int(input("enter second number not zero : "))
# # except ZeroDivisionError:
# #     print('second number must not be zero')
# except ZeroDivisionError as err:
#     # it will print the default error
#     print(err)
# except NameError:
#     print("please enter numbers only")

# except :
#     print("unexpected error")

# def divide(a,b):
#     return a/b

# print(divide(num1, num2))


# python custom exception
# why custom exception
# to increase the readability of the code

class NameTooShort(ValueError):
    pass

def validate(name):
    if len(name) < 8:
        # raise ValueError ("name too short")
        raise NameTooShort ("name too short")

    
user_name = input("enter your name: ")
validate(user_name)
print(f'hello {user_name}')
# ValueError: name too short
# what if we want NameTooShort : name too short error 