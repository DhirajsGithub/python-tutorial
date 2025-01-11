# # class methods

# class Person:
#     # class variables
#     count_instance = 0
#     # defining method
#     def __init__(self, first_name, last_name, age):
#         # that's how we use class vaiable
#         Person.count_instance += 1
#         # instance variables
#         self.first_name  = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full_name = first_name+" "+last_name

# p1 = Person("harshit", "vashishtha", 34)
# p2 = Person("naman", "deore", 22)

# that's how we use class methods
# Person.method_name()    #or   p1.method_name()
# but we can use instance only like p1.method_name()


# note in instance method first argument is object/instance itself
# but in class method first argument is class (cls)

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

        # we use decorator to create class method python main pahale se hi bana huae hain decorator
    @classmethod
    def count_instances(cls):                               # cls is convention which means iss class main dekho
        # return f"you have created {cls.count_instance} methods/instances of Person class "
        return f"you have created {cls.count_instance} methods/instances of {cls.__name__} class "


    # creating instance methods
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    #creating instance methods
    def is_above_18(self):
        return self.age >= 18




p1 = Person("harshit", "vashishtha", 34)
p2 = Person("naman", "deore", 22)
print(Person.count_instances())
print(p1.count_instances())              #the reason why these acces caz pahale agar object ne method ko call kiya toh python pahale check karega ki kya ye instance method hain agar nahi toh woh class method main check karega
