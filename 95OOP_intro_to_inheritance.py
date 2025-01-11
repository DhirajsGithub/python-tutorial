# inheritance

# from _typeshed import SupportsItemAccess


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = price

    def make_a_call(self, phone):
        print(f"calling phone.no {phone}....")
    
    def full_name(self):
        return f'{self.brand} {self.model_name}'

# now we want to make a class(derived / child class) which have all the features of class phone(parent class) + additio of itself
# inheritance will also takes the methods of the parent class 

class Smartphone(Phone) :
    def __init__(self, brand, model_name, price, ram, internal_memory, real_camera):
        # # m-1 ----> uncomman way
        # Phone.__init__(self, brand, model_name, price)
        # m-2
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.real_camera = real_camera

    # defining new methods for smartphone
    def sepcification(self):
        return f'ram is {self.ram} camera is {self.real_camera}'

phone = Phone("nokia", "1100", 1100)
# print(phone.full_name())
# phone.make_a_call(9923253629)

smartphone = Smartphone("one plus", "5", 30000, '6GB', '128GB', '64MP')
smartphone.sepcification()
print(smartphone.full_name())