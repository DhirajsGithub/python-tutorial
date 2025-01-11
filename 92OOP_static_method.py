# static method 
# static methods are not related to our class nor our instance(object)
# A static method can’t access or modify the class state.
# It is present in a class because it makes sense for the method to be present in class.

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
        return cls(first, last, age)

    # creating class method
    @classmethod
    def count_instances(cls):                               
        return f"you have created {cls.count_instance} methods/instances of {cls.__name__} class "

    # creating static method
    @staticmethod
    def hello():
        print("static method, called !!!")
  
    # creating instance methods
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    #creating instance methods
    def is_above_18(self):
        return self.age >= 18

p1 = Person("harshit", "vashishtha", 34)
p2 = Person("naman", "deore", 22)
Person.hello()


#################### upto this point ##########################
class Animal:

    # class variabls 
    price = 40
    var = "this is class "
    instance_number = 0

    # constructor function
    def  __init__(self, name, age, breed):
        Animal.instance_number +=1
        self.animalName = name
        self.animalAge = age
        self.animalBreed = breed

    # instance function which will be limited to class object/instance
    def full_name(self, s):
        return "animal name is {} animal age is {} something is {}".format(self.animalAge, self.animalAge, s)

    @classmethod
    def class_method(cls, s):
        return cls.var + cls.__name__ +" "+s
    
    @staticmethod
    def static_method(s):
        print("useless method", s)

    # instance mehtod
    def animal_price(self):
        # using self to access class variable leads to change in variable if that class variable is change for that instance
        print(f"Animal: {self.animalName} price is ${self.price}, with age {self.animalAge}")
        print(f"Animal: {self.animalName} price is ${Animal.price}, with age {self.animalAge}")
    
    @classmethod
    def count_instnace(cls):
        print(f"count instnce is {cls.instance_number}")
    
    # creating our own constructor
    @classmethod #imp
    def split_animal(cls, string):
        name, age, breed = string.split(",")
        return cls(name, age, breed)
 

# cat instance
cat = Animal("meens", 2, "shit1")
print(cat.animalAge)
print(cat.full_name("she is cute"))
print(cat.class_method("sheee"))
Animal.static_method(44)
cat.static_method(44)
cat.animal_price()
cat.price = 20
cat.animal_price()

dog = Animal("sunyaa", 7, "shit2")
dog.animalBreed = "Shit3"
print(dog.animalBreed)
Animal.count_instnace()

mouse = Animal.split_animal('jerry,d,shit6')
print(mouse.full_name("mousy"))
print(mouse.animalBreed)
print(mouse.animalName)
