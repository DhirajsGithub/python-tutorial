#default parameters:

# def user_info (first_name, last_name, age):
#     print(f"user first name is {first_name}")
#     print(f"user last name is {last_name}")
#     print(f"your age is {age}")

# user_info("harshit", "vahishtha", 67)
##ye ho gaya normal function jaha har yek parameter ke liye argument define hai

def user_info (first_name, last_name='unknown', age = None):
    print(f"user first name is {first_name}")
    print(f"user last name is {last_name}")
    print(f"your age is {age}")

#user_info("harshit", "vahishtha", 45)  #note agar apne default parameters set kiye hai aur arguments aap dusre dal rahe ho toh argument overcome karege default parameters ko !
user_info("harshal")   #note apbhi first name harshal print hoga last name unknown and age None print honge
# very impt note: apn default parameter follow by none default parameters nahi kar sakte. 
# apn sab parameters default kar sakte hain

# NOTE: def user_info (first_name = 'unlnown', last_name, age ): yaise nahi kar sakte
