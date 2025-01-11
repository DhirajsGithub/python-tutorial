# special / magic method / dunder method
# operator overloading
# polymorphism

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = price
    
    def phone_name(self):
        return f'{self.brand} {self.model_name}'

    # str, repr (for output the same as the object/instance is equal to )
    def __str__(self):
        return f'{self.brand} {self.model_name}'
    def __repr__(self):
        # return f"{self.brand} {self.model_name} {self._price}"
        return f"Phone(\"{self.brand}\", '{self.model_name}', {self._price})"
    
    # len (to measure the length of our method
    def __len__(self):
        return len(self.phone_name())
    
    # operator overloading (to apply operations on any variable of the objects)
    def __add__(self1, self2):       # we ill pass to object for operation hence consider self1 and self2
        return self1._price + self2._price
    
class Smartphone(Phone):
    def __init__(self, brand, model_name, price, camera):
        super().__init__(brand, model_name, price)

    def __len__(self):
        return self._price

l = [1,2,3,4]
print(l)            # [1, 2, 3, 4]  how we get such result from our self made classes

my_phone = Phone("nokia", '1100', 1000)
print(my_phone)             #--(1)        # <__main__.Phone object at 0x1036761f0>  expected Phone("nokia", '1100', 1000)
# for that we have str and repr method which will print whatever we return through them by simply print object name
# by (1)  only str will be called if both str and repr object are present
# we can also called str and repr as we call for methods
print(my_phone.__repr__())
# print(str(my_phone))
# print(repr(my_phone))
# str is for normal user and repr is for dev for debuging shit.
print("---------len--------")
l = [1,2,3,4]
print(len(l))

print(my_phone.__len__())

print("--------operation-------")
my_phone2 = Phone("nokia", '1600', 1200)

print(my_phone2 + my_phone)

print("---------polymorphism---------")

# The literal meaning of polymorphism is the condition of occurrence in different forms. 
# Polymorphism is a very important concept in programming. It refers to the use of a
# single type entity (method, operator or object) to represent different types in different scenarios.
my_smartphone = Smartphone("one plus", "6T", 30000, '64MP')
print(my_smartphone.__len__())
print(my_phone.__len__())

# len method from 65 and 66 does other task but name is same hence it is called polymorphism 