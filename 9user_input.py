#user input
#input function

# name = input("type your name ")          #note: very imp :input hamesha string main liya jata hai
# print("hellow "+ name)                     
# age = input("what is your age ")
# print("your age is "+ age)  #no error                #shows that input taken is in form of string

# name, age = input("enter your name and age separated by spaces only").split()   #user ko name and space dalni padegi with one or maore than one spaces
# print(name)
# print(age)   

name, age = input("enter your name and age separated by comma only").split(",")   #user ko name and space dalni padegi with one comma
print(name)
print(age)  

x, y, z, m = ("x,y,z,m").split(",")
print(x,y,z,m)

# note split() function ko yaise samjho agar space ya comma ya any other character hain in (" ") then uske ajun baju se split ho jayega 
# split method will spilt the iterable accordingly and return a list of it by default
# Joining a string is simple:

# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings. 
# >>> print a
# ['this', 'is', 'a', 'string']
# >>> a = "-".join(a)   # with this method we can join items of list as well
# >>> print a
# this-is-a-string 

# a.split(" ",2)    will split 2 comma spearated values 