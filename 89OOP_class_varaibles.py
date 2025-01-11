# class variables

# instance variables(attribute) are unique for all objects
# class variables(attribute) share with all the objects

# making a class circle
class Circle:
    # defining a class varibale
    pi = 3.14
    # defining an object
    # def __init__(self, radius, pi):
    def __init__(self, radius):
        # instance variables 
        self.radius = radius
        # self.pi = pi
    
    #defining an object for cal circumference
    def cal_circumf(self):
        # return 2*self.pi*(self.radius)
        return 2*Circle.pi*(self.radius)
        # if we know such varaible is only present in class and all object have value same to such variable in a class variable and it can be only access by class_name.variable_name in methods of class

 
# c1 = Circle(4, 3.14)
# c2 = Circle(5, 3.14)

c1 = Circle(4)
c2 = Circle(5)
print(c1.cal_circumf())


# # class laptops
# class Laptop:
#     #applying a fixed discound to all objects
#     discount_percent = 20
#     # creating init method
#     def __init__(self, name, brand, price):
#         # instance variables
#         self.lap_name = name
#         self.lap_brand = brand
#         self.lap_price = price
#         self.info = (f"laptop name is {name} brand is {brand} price is {price}")

#     # method(function) to apply the discount
#     def apply_discount(self):
#         off_price = (self.lap_price*(Laptop.discount/100))
#         return self.lap_price - off_price


# lap1 = Laptop("Mackbook Air", "M1-chip", 91000)
# lap2 = Laptop("Lenova", "yoga-103", 80000)
# print(lap1.apply_discount())


# class variable fluctuating for some objects
# class laptops 
class Laptop:
    #applying a fixed discound to all objects
    discount_percent = 20
    # creating init method
    def __init__(self, name, brand, price):
        # instance variables
        self.lap_name = name
        self.lap_brand = brand
        self.lap_price = price
        self.info = (f"laptop name is {name} brand is {brand} price is {price}")

    # method(function) to apply the discount
    def apply_discount(self):
        # off_price = (self.lap_price*(Laptop.discount_percent/100))            #----(1)
        off_price = (self.lap_price*(self.discount_percent/100))              #------(2)
        return self.lap_price - off_price


# Laptop.discount_percent = 0                      #sell khatam ho gayi :)
lap1 = Laptop("Mackbook Air", "M1-chip", 91000)
lap2 = Laptop("Lenova", "yoga-103", 80000)
print(lap1.apply_discount())                            #72800.0(20% wala discount)
print(lap1.__dict__)                        # will give all lap1 instance variables

# print(lap2.apply_discount())       # ----(3)        #64000.0 (discount of 20% from (1))
# we want laptop2 dicount percent be 50 then 
lap2.discount_percent = 50       #----(4)        #it will create a instance variable as discount_percent : 50 
print(lap2.__dict__)               
# print(lap2.apply_discount())   # no change similar to (3)   # though instance variable added yet apply discount is consider for class variable 
# but if we create off_price lke in (2) like using self but defing variable in class then python pehele check karega kya discount_percent instance varaible object ke pass hain agar nahi toh woh class variable ke pass jayega

print(lap2.apply_discount())          # 40000.0 (discount of 50% from (2) and (4) 