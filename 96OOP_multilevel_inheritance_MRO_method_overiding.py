# can we derive more than one class from base class 
# yes we can derive more than one class from the same base class
# like class Phone can have class Smartphone, class Smarthphone2, ....

# multilevel inheritance
# method resoultion order (MRO)
# method overiding
# isinstance(), issubclass()

import builtins


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = price

    def make_a_call(self, phone):
        print(f"calling phone.no {phone}....")
    
    def full_name(self):
        return f'{self.brand} {self.model_name}'

class Smartphone(Phone) :
    def __init__(self, brand, model_name, price, ram, internal_memory, real_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.real_camera = real_camera

    # defining new methods for smartphone
    def full_name(self):
        return f'{self.brand} {self.model_name} with ram {self.ram} and real camera {self.real_camera}'

# multilevel inheritance
class FlagshipPhone(Smartphone):
    def __init__(self, brand, model_name, price, ram, internal_memory, real_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, real_camera)
        self.front_camera = front_camera
    
    def full_name(self):
        return f'{self.brand} {self.model_name} with ram {self.ram} and real camera {self.real_camera} and front camera {self.front_camera}'


phone = Phone("nokia", "1100", 1100)
smartphone = Smartphone("one plus", "5", 30000, '6GB', '128GB', '64MP')
smartphone.full_name()

super_phone = FlagshipPhone("redmi", "note-7 PRO", 15000, '4GB', "64GB", "32MP", "16MP")
print(smartphone.full_name())
print("-------------------------")

# method resolution order (MRO)
# print(help(smartphone))  
# the order in which python searches our method and our instance variables like for smartphone it is
# Smartphone
# Phone
# builtins
# builtins is the class fron which all the classes of python are inherited like a super of super class

# print(help(super_phone))
# for supher_phone the order is
# FlagshipPhone
# Smartphone
# Phone
# builtins
   

print("------------------------")
# method overriding
print(super_phone.full_name())     # overriding over class Smartphone full_name and Phone full_name
print(smartphone.full_name())      # overriding over class Phone full_name

print("------------------------")
# isinstance
print(isinstance(phone, Phone))         # True phone is the object of class Phone
print(isinstance(smartphone, Phone))    # True smartphone is the object of class Phone
print(isinstance(super_phone, Phone))    # True 

print(isinstance(super_phone, Smartphone))     # True     
print(isinstance(smartphone, Smartphone))       # True
print(isinstance(phone, Smartphone))            # False      phone is not the object of class Smartphone
print(isinstance(smartphone, FlagshipPhone))     # False


print("------------------------------")

print(issubclass(Smartphone, Phone))        # True Smarthphone class is the subclass of the class Phone

print(issubclass(FlagshipPhone, Phone))         # True
print(issubclass(FlagshipPhone, Smartphone))     # True

print(issubclass(Smartphone, FlagshipPhone))     #False