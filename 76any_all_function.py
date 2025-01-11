#any_all_function
numbers1 = [2,6,8]
numbers2 = [0,2,1,3,5,7,10]

evens = []
for num in numbers1 :
    evens.append(num%2==0)

# all
print(evens)
print(all(evens))      #checks for all the element whic holds the property

# with list comprehension
print(all([num%2==0 for num in numbers1]))

# any 
print(any([num%2==0 for num in numbers1]))
print(any([num%2==0 for num in numbers2]))


# modified sum function if argument is not string/float
def sum_all (*args):
    if all([type(arg) == int or type(arg)==float for arg in args]):   #note or with type yaise hi lagta hain. don't use int or float
        total = 0
        for num in args :
            total += num
        return total
    else :
        return "wrong input"
    
print(sum_all(2,3,4,6,"harshit"))