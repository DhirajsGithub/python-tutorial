# instance(object) methods
l = [1,2,3,4]
# python main list class pahale se hi bani huae hian apn ne sirf uss class ka yek instance(object) create kiya (l)

class Person :
    def __init__(self, first_name, last_name, age):
        #instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    # creating instance methods
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    #creating instance methods
    def is_above_18(self):
        return self.age >= 18

p1 = Person("harshit", "sharma", 24)
# that's how we access instance methods
print(p1.full_name())                   # object(instance).method()
print(Person.full_name(p1))        # actual what's happening  class_name.instance_mehtod(object(instance))
print(p1.is_above_18())
# self ko yaisa samjho ki is class main jo object hain waha ke varaibles ko lena hain naya argument pass karna jaruri nahi yaisa 

# we define init method and first argument in it is object but while creating p1 object we didn't pass an object
# python khud self object ko define karva deta hain

# koi bhi method class ke under function ki tarah hota hain and pahala argument unme self(conventionally) compulsary hoga

li = [1,24,43,5,7,8]
# li.clear()                #li is the object of class list as like p1 the object of class Person
# print(li)                 #and clear is it's method like init, full_name, is_about_18 
# list.clear(li)            # here li is self 
# print(li)

li.append(29)
print(li)                           # as we pass self in object of Person just like we pass li
list.append(li, 29)
print(li)


# create a class which counts the number of instance it has
class Persona:
    #defining the method:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Persona.count_instance +=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    

p1 = Persona('harsh', 'lad', 23)
p2 = Persona('hars', 'lad', 22)
p3 = Persona('har', 'lad', 233)
p4 = Persona('ha', 'lad', 21)
print(Persona.count_instance)                      

