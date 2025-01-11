# Exception handling
# try except

# handle error if user inters age as seven instead of 7

while True:
    # to run the code while user inputs the right value 
    try:
    # try this code if age is int then the loop will break
    # all varaible will be define in try itself 
        age = int(input("enter your age : "))
        break

    except ValueError:
    # this except will handle the eroor like ValueError which has more chance at try to be raised
        print("try using int as input, please")
    
    except :
    # this except will handle rest of the errors
        print("unexpected error")

# note: we used two excepts caz agar ValueError ata hain toh python direct ValueError wala loop chalayega and use classes main dusre error ko khonjne ki jarurat nahi padegi


if age >= 18:
    print("you can play the game")
else :
    print("you can not play the game ")