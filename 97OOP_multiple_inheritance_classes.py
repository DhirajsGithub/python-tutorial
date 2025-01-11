# multiple inheritance classes

class A :
    def class_a_method(self):
        return 'I\'m just a class A method'
    
    def hello(self):
        return 'hellow from class A'

# instance_a = A()
# print(instance_a.class_a_method())


class B :
    def class_b_method(self):
        return 'I\'m just a class B method'
    
    def hello(self):
        return 'hellow from class B'

class C(A,B):
    pass

instance_c = C()
print(instance_c.class_a_method())
print(instance_c.hello())               # hello from class A is printed caz due to MRO
# print(help(instance_c))
# MRO order of class C is 
# C, then A, then B then builtins.object      we can change this by changing inheritance of (A, B)  for class C

# finding MRO order 
print(help(C))
print(C.mro())          # list
print(C.__mro__)        # tuple















