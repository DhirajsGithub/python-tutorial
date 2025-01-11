# kwargs (keyword arguments)
# when we are decipher for the numbers of arguments and store alll argument in dictionary
# convection hain isliye use karte hain 'kwargs'
# **kwargs double star argument

# kwargs as a parameter :
def func(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    # **kwargs will give dictionary 
    for k, v in kwargs.items():
        print(f"{k} : {v}")

func (first_name = "harshit", last_name = "vashishtha")       #note dict lagaya nahi matlab woh ditionary main convert hua hain lekin unpack bhi ho gaya hain
# d = dict(first_name = "harshit", last_name = "vashishtha")
# func(**d)
# d = {'first_name' : "harshit", 'last_name' : "vashishtha"}
# func(**d)
# bat ki gaharayi ko samjho bhai !

def func_2(name, **kwargs):
   for k, v in kwargs.items():
        print(f"{k} : {v}")

d = { 'first_name_2' : "Harshal", 'age' : 22}

# func_2("mohit", d)    #error
# dictionary unpacking
func_2("mohit", **d)