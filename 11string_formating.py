name = "Harshit"
age = 24

# print("hellow "+name + " "+ "your age is "+str(age))   #ugly syntax

#string formating 
#python 2
#python 3
#python 3.6(best)

print("hellow {} your age is {}".format(name, age+2))     #python 3
#remember that .format yaha pr data types konse jod rahe hai unke fikar karne ki jarurat nahi hai

print(f"hellow {name} your age is {age}")           #python 3.6
#remember that f yaha pr data types konse jod rahe hai unke fikar karne ki jarurat nahi hai


# You can add parameters inside the curly brackets to specify how to convert the value:
x = 53
txt = "The price is {:.2f} dollars"
print(txt.format(x))

print("the binary of 11.5 is {:b}".format(x))
