class Phone:
    def __init__(self, brand, model_name, price, discount):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)            #for considering the price > than 0 # or we can use if else statement
        # self._price = price
        self.__discount = discount
        # self.complete_specefictn = f"{self.brand} {self.model_name} price is{self._price} "


        # getter() and setter() pahale property(jo ki getter hota hain) then use setter
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)
    
    # def complete_specefictn(self):
    #     return f"{self.brand} {self.model_name} price is {self._price}"
    @property
    def complete_specefictn(self):
        return f"{self.brand} {self.model_name} price is {self._price}"


    def make_a_call(self, phone):
        print(f"calling phone.no {phone}....")
    
    def full_name(self):
        return f'{self.brand} {self.model_name}'

phone1 = Phone("nokia", "1100", -1000, 30)
print(phone1.brand)
print(phone1.model_name)
print(phone1._price)
# print(phone1.price)             # 1.since we have use getter and line 12 so no need to use _price
print(phone1.complete_specefictn)
print("------------1--------------")
phone1._price = 500        # updated price
print(phone1._price)
# print(phone1.price)             # since we have use getter at line 12 so no need to use _price
# print(phone1.complete_specefictn)
# 2.price is changed at line 35 but not at line 37 caz it will consider the price of the object 
# caz jab bhi init method call hoga tabhich complete_specefictn wala variable create ho jayega and isliye woh bad main update na ho payega
# so better we create a new instance method for it 
# print(phone1.complete_specefictn())                # from line 19
print(phone1.complete_specefictn)                   # from line 21

print("-------------------2-------------------")
phone1._price = -500
print(phone1.complete_specefictn)                       # it will print the updated -500 so how to deal with it we have getter() and setter() method
print('-------------------3--------------------------')
phone1.price = -500                             #note agar getter() and setter use kar rahe ho toh private name ka syntax na use karna
print(phone1.complete_specefictn)           # note 50 and 54 line


# As the name suggests, getters are the methods which help access the private attributes or 
# get the value of the private attributes and setters are the methods which help change or 
# set the value of private attributes. ...