# f = open('practise.txt', 'r')
# print(f.tell())
# print(f.read())
# f.seek(0)
# print(f.read())

# print(f.tell())

# print(f.readline())
# print(f.readline())

# lines = f.readlines()
# for line in lines:
# #     print(line, end='')
# f = open("/Users/dhiraj/Library/Mobile Documents/com~apple~CloudDocs/python_tutorials/for read txt/test_file.txt") 
# # print(f.readlines())
# for line in f:
#     print(line)

# print(f.name)
# print(f.closed)
# f.close()
# with open('105text.txt') as f:
#     # var = f.read()
#     data = f.read()
#     print(data)

# print(f.closed)

# with open('practise.txt', 'a') as rf:
#     rf.write('hellow')

# reading large files with small chunks 
# with open ('109large.txt', 'r') as rf:
#     data = rf.read(100)
#     while(len(data)>0):
#         print(data)
#         data = rf.read(100)


# csv reader 
# from csv import reader
# with open('110file.csv', 'r') as rf:
#     data = reader(rf)      # iterator
#     # print(data)
#     print(next(data))
#     print(next(data))

# csv DictReader
# from csv import DictReader
# with open('110file.csv', 'r') as rf:
#     csv_reader = DictReader(rf)
#     # print(csv_reader)
#     print(next(csv_reader))
#     print(next(csv_reader))
#     print(next(csv_reader))
#     print(next(csv_reader))

# write in csv file
# from csv import writer

# with open('112file.csv', 'w', newline='') as wf:
#     write = writer(wf)
#     write.writerows(([['class', 'education'], ['4', 'B.tech']]))


# Encapsulation
# refers to the bundling of data, along with the methods that operate on that data, into a single unit. Many programming languages use encapsulation frequently in the form of classes.
# Mangling
# Abstraction
# _name convention
# showing only essential attributes and "hides" unnecessary information. The main purpose of abstraction is hiding the unnecessary details from the users.
# In name mangling process any identifier with two leading underscore is textually replaced with _classname__identifier
# to told the developer that it is a private property/instance variable so don't change it
# self._price = price

# class Phone :
#     def __init__(self, name, brand, price):
#         self.name = name
#         self.brand = brand
#         self._price = max(price, 0)
#         # self.specification = f"{self.name} {self.brand} cost {self._price}"
    
#     @property
#     def specification(self):
#         return f"{self.name} {self.brand} cost {self._price}"

#     @property
#     def updatePrice(self):
#         return self._price
#     @updatePrice.setter 
#     def updatePrice(self, newPrice):
#         self._price= max(newPrice, 0)
    


# phone1 = Phone("nokia", "1100", -1000)
# phone1.updatePrice = -500
# # print(phone1.specification) #nokia 1100 cost 1000 #price didn't update
# # print(phone1.specification())
# print(phone1.specification)
# phone1.updatePrice = 20000
# print(phone1.specification)

# class Phone :
#     instance = 0
#     def __init__(self, name, model, price):
#         self.name = name
#         self.model = model
#         self.price = price
#         Phone.instance += 1
#     def make_a_call(self, number):
#         return f"calling {number}...."
    
# class SmartPhone(Phone):
#     def __init__(self, name, model, price, ram, camera):
#         super().__init__(name, model, price)
#         self.ram = ram
#         self.camera = camera
#     def specification(self):
#         return f"ram is {self.ram} camer is {self.camera} MG"

# phone1 = Phone("Nokia", "1100", 1100)
# print(phone1.make_a_call(8811971479))
# smartphone1 = SmartPhone("one plus", "5", 30000, '6GB', '64MP')
# print(smartphone1.make_a_call(2498932900))
# print(smartphone1.specification())
# print(Phone.instance)
# # print(SmartPhone.instance)

 
class A :
    def class_a_method(self):
        return 'I\'m just a class A method'
    
    def hello(self):
        return 'hellow from class A'

class B :
    def class_b_method(self):
        return 'I\'m just a class B method'
    
    def hello(self):
        return 'hellow from class B'

class C(A,B):
    pass

instance_c = C()
print(instance_c.class_a_method())
print(instance_c.hello()) 
print(list(C.mro()))          # list
# print(list(C.__mro__))