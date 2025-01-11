# else and finally clause in exception handling

# while True:
#     try:
#         age = int(input("enter your age : "))
#         break

#     except ValueError:
#         print("try using int as input, please")
    
#     except :
#         print("unexpected error")

# if age >= 18:
#     print("you can play the game")
# else :
#     print("you can not play the game ")

from typing import final


while True:
    try:
        num = int(input("enter your number : "))
        # break

    except ValueError:
        print("try using int as input, please")
    
    except :
        print("unexpected error")
    
    else :
    # will run if try is true i.e. if no exception occur
    # provided try has no break
        print("user input {}".format(num))
    
    finally:
    # finally clause always runs whether error/ exception occurs or not
        print("finally block runs .....")