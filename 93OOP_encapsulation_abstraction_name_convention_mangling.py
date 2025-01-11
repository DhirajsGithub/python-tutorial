class Phone:
    def __init__(self, brand, model_name, price, discount):
        self.brand = brand
        self.model_name = model_name
        self._price = price
        self.__discount = discount

    def make_a_call(self, phone):
        print(f"calling phone.no {phone}....")
    
    def full_name(self):
        return f'{self.brand} {self.model_name}'

phone1 = Phone("nokia", "1100", 1000, 30)
    

# Encapsulation: write our data and the functions to be perform with that data at the same place is known as encapsulation
# Encapsulation in OOP Meaning: In object-oriented computer programming languages, the notion of encapsulation (or OOP Encapsulation)
# refers to the bundling of data, along with the methods that operate on that data, into a single unit. Many programming languages use encapsulation frequently in the form of classes.

l = [2.56,3,57,1,0,3,5]
l.sort() #tim sort. bahut sare algorithm hote hain sorting ke toh woh kuchh hame dikahyi nayidete hamm sirf sort method ko easily use kar lete hain

# Abstraction: hiding of all the complexity the method has
# Abstraction is the concept of object-oriented programming that "shows" only essential attributes and "hides" unnecessary information. 
# The main purpose of abstraction is hiding the unnecessary details from the users. ... It is one of the most important concepts of OOPs

# _name convention for private name(convention)
# naming conventin line 5 price is writtern as _price to told the developer that it is a private property/instance variable so don't change it
# python main kuch private nahi hain sab public hain

# __name__  ---> dunder / magic methods

# name mangling  In Python, mangling is used for class attributes that one does not want subclasses to use which are designated as such by giving them a name with two leading underscores and no more than one trailing underscore.
# print(phone1.__discount)       # error
print(phone1.__dict__)   #{'brand': 'nokia', 'model_name': '1100', '_price': 1000, '_Phone__discount': 30}
# we see that __discount instance varaible name is change to _Phone__discount
print(phone1._Phone__discount)     # 30      from line 6