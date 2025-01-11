# Object oriented programming
# comman topic in almost all popular languages with comman idea but different syntax
# OOP is just a style/ way to write our code which makes it easier to read it, it won't enhance the code runtime
# very helpful in creating real world programs
# classes, object(instance), method

l = [2,34,5,6,6]
# l is the object of class list  
# append is the method 
l.append(8)           #object.method()     #methods are define like function

# python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# we create classes to make our own methods
# class person
class Person:                                               # class name convectionally start with capital letter
    # creating constructor/init                             # All classes have a function called __init__(), which is always executed when the class is being initiated.
    def __init__(self, first_name, last_name, age):         # we create init method (built-in __init__() function.), jab bhi apn object ko call karege init method khudse active hoga. self is convention to write
        #instance(object) variables                         # instance method main jo first argument hoga woh hoga hamara object/instance khud (self), init method ko contructor bhi kahate dusre lan main like JS
        print("init method// constructor get called")       # self ke bad jo arguments hain woh class ke attribute hote hain
        self.person_first_name = first_name                 # Objects can also contain methods. Methods in objects are functions that belong to the object.
#                                                           # Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
        self.last_name = last_name
        self.age = age
        self.full_name = first_name +" " + last_name

p1 = Person("harshal", "sharma", 32,)                       # p1, p2 are the objects of the classs Person
p2 = Person("Rohit", "kohli", 34)                           # object.(...)  will give all the methods available in class
                                                        
# print(p1.person_first_name)                                        # jab object call hoga tab init method call hoga
# print(p2.age)
# print(p2.last_name)
# print(p1.full_name)


# class laptops
class Laptop:
    # creating init method
    def __init__(self, name, brand, price):
        # instance variables
        self.lap_name = name
        self.lap_brand = brand
        self.lap_price = price
        self.info = (f"laptop name is {name} brand is {brand} price is {price}")

    # method(function) to apply the discount
    def apply_discount(self, discount):
        if discount <40:
            return f"price after applying discount is{(self.lap_price) - (self.lap_price*(discount/100))}"

lap1 = Laptop("Mackbook Air", "M1-chip", 91000)
lap2 = Laptop("Lenova", "yoga-103", 80000)

# print(lap1.lap_price)
# print(lap1.lap_brand)
# print(lap2.lap_name)
# print(lap1.info)
print(type(lap1.lap_price))

print(lap1.apply_discount(30))