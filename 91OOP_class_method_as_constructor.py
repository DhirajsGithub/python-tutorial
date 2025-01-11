# class method as constructor

# class Person :
#     def __init__(self, first_name, last_name, age):
#         #instance variables
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     # creating instance methods
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#     #creating instance methods
#     def is_above_18(self):
#         return self.age >= 18

# p1 = Person("harshit", "sharma", 24)
# this is the object in which added attribute as comma sepearted but in different strings/ datatypes which have init method above

# agar apn ko yaisa object babnana ho jo ki yek hi string main sare attribut le toh apn ko apna constructor / init method banana padega
class Person:
    # class variables
    count_instance = 0
    # defining method
    def __init__(self, first_name, last_name, age):
        # that's how we use class vaiable
        Person.count_instance += 1
        # instance variables
        self.first_name  = first_name
        self.last_name = last_name
        self.age = age

    # creating our own constructor
    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(",")
        # same as __init__(self, first_name, last_name, age)
        return cls(first, last, age)

    # creating class method
    @classmethod
    def count_instances(cls):                               
        return f"you have created {cls.count_instance} methods/instances of {cls.__name__} class "


    # creating instance methods
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    #creating instance methods
    def is_above_18(self):
        return self.age >= 18

p1 = Person("harshit", "vashishtha", 34)
p2 = Person("naman", "deore", 22)
# p3 = Person("harshal, jaiswal, 22")
# # print(p3.full_name())           # error 
p3 = Person.from_string("harshal, jaiswal, 22")
print(p3.full_name()) 