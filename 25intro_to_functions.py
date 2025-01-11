#functions
#we can store anything in function define what it does and call it whenever needed

#defining a function
def add_two (a,b) :
    return a+b

#call a function 
total = add_two(4,5)
print(total)

join = add_two("Har", "shal")
print(join)

a = int(input("enter any number"))
b = int(input("enter another number or whatever who cares she is just hurt me, making me fucking sick"))
print(add_two(a,b))


#print vs return :
def add_three(a,b,c):
    print(a+b+c)

add_three(4,4,4)
#note agar apn ne print likhe function ko define karte samai then bad mai print likhne ki jarurat nahi hai