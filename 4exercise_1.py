# print("this is \\\\ double slash")
# print("this are /\\/\\/\\/\\ mountains")
# print("he is \t awesome")
# print("\\\" \\n \\t \\\'")

# #Q.ask user to input three numbers and print there average

# num1, num2, num3 = (input("enter three number seperated by spaces ")).split()
# average = ((int(num1) + int(num2) + int(num3))/3)
# print(f"average of three numbers is {average}")


#Q.ask for user name and print in reverse order

# name = input("What is your name?")
# print("your name in reverse oorder is "+name[::-1])


# # Q. take two comma separaed inputs from user i.e. username and any single character
# # now count the characters that at in username and also which user inputed separatly
# username, anyletter = (input("enter your name and any lettter comma separated")).split(",")
# print(f"number of characters in your name are {len(username)} your input counted in username are {username.count(anyletter.upper()) + username.count(anyletter.lower()) }")

# #note: for our above example if user add space in between name and letter with comma it will be error to solve this error
# user_name,any_letter = (input("enter your name and one letter comma separated")).split(",")
# print(f"your name count character are {len(user_name.strip())}")
# print(f"character count of your input letter{ user_name.count(any_letter.strip().upper()) + user_name.count(any_letter.strip().lower()) }")

user_name, age = input("enter your name and age comma separated").split(",")
user_name = user_name.strip()
age = int(age)
if user_name[0]== ("a" or "A") and age >=10 :
    print("you can watch coco movie")
else:
    print("you can't watch coco movie")