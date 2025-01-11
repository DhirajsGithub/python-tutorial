# example 1

class Animal:
    def __init__(self, name):
        self.name = name

    #abstract method (jo kuch nahi karta sirf error raise karta hain taken from java)
    def sound(self):
        # NotImplementedError
        raise NotImplementedError ("You have to define sound of specific animal in it's class")

    
class Dog(Animal):
    def __init__(self, name, bread):
        super().__init__(name)
        self.bread = bread
    
    # def sound(self):
    #     return "bhow bhow !!"
    
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def sound(self):
        return "meow meow !!"
    

# we know according MRO first method will be check at sub class the it will go to parent class if absent in subclass
# we raise a error in parent class of method soud such that if sound method does not exist in subclass it will go to 
# parent class and hence error  will be raised ! hecnce we need to create sound method in subclass

doggy = Dog("tommy", 'Pug')
print(doggy.bread)
# print(doggy.sound())      # error raised !


# example 2
print("-----example-2----------")

class Mobile_store_1:
    def __init__(self, name):
        self.name = name

class Mobile_store_2:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, new_moibile):
        # but we want jo mobile Mobile_store_1 insatnce ke pass hain wahi mobiles main aye else error raise ho jaye
        if isinstance(new_moibile, Mobile_store_1):
            self.mobiles.append(new_moibile)
        else:
            raise TypeError ("new mobile should be object of Mobile_store_1 class")

        
    
oneplus = Mobile_store_1("one plus 6")
print(oneplus.name)
samsunng = "samsung galaxy s8"
mobo_store = Mobile_store_2()
print(mobo_store.mobiles)

# mobo_store.add_mobile(samsunng)        # error raised
# print(mobo_store.mobiles)

mobo_store.add_mobile(oneplus)

mobo_phone = mobo_store.mobiles
print(mobo_phone[0].name)

