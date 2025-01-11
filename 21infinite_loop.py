#infinite loop

# #infinite loop by mistake if i is not updating
# i=0
# while i<=10 :
#     print("hellow world")

# from _typeshed import FileDescriptor


# while True:
#     print("Hellow world")


#modify number guessing game
import random
winning_num = random.randint(1, 100)

winning_num = 67
num = int(input("guess a number "))
guess = 1
game_over = False
while not game_over:
    if num == winning_num:
        print(f"you win after {guess} trials")
        game_over = True
    else:
        if num>winning_num:
            print("hight")
        else: 
            print("low")
        
        guess += 1
        num = int(input("guess again "))
# DRY - don't repeat yourself

# winning_num = 54
# num = int(input("guess a number"))
# guess = 1
# game_over = True
# while game_over:
#     if winning_num == num:
#         print("you win")
#         game_over = False
#     else:
#         if num>winning_num:
#             print("hight")
#         else: 
#             print("low")
        
#         guess += 1
#         number = int(input("guess again "))    


