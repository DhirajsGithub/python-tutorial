#function returning function

def outer_funct():
    def inner_funct():
        print("inside inner funct")
    
    return inner_funct

var = outer_funct()
var()

def outer_funct_2(msg):
    def inner_funct_2():
        print(f"message is {msg}")
    return inner_funct_2

var_2 = outer_funct_2("Hi there")
var_2()


# function returning function (CLOSURE) practise
def to_power (x):
    def to_base(n):
        return  n**x
    
    return to_base

cube = to_power(3)         #to_power wala function to_base return kar raha hain
print(cube(2))             #jo to_base return ho raha hain usko argument di


# note jab to_base call hoga toh woh to_power ke parameter and jiite bhi variable hain to_power main unko lekar return hoga
