#list comprehesion with if statement
numbers = list(range(1,11))
#create a list which stores all even numbers
even_nums = []
for i in numbers :
    if i%2==0:
        even_nums.append(i)

print(even_nums)

# even numbers 
even_nums_short = [i for i in numbers if i%2==0]
print(even_nums_short)
even_nums_short_2 = [i for i in range(1,11) if i%2==0]
print(even_nums_short_2)

#odd numbers 
odd_nums_short = [i for i in range(1,101) if i%2 != 0]
print((odd_nums_short))

#num to string 
# define a function which takes any input and returns numbers as string 
# def num_to_string (l):
#     empty_list = []
#     for i in range(0, len(l)):
#         if (type(l[i]) == int or type(l[i])==float):
#             empty_list.append(str(l[i]))
#         return empty_list

# print(num_to_string([2,2,3.0,False,None,[2,3,4.0]]))
    
def num_to_string (l):
    return [str(i) for i in l if (type(i)==int or type(i)==float)]
print(num_to_string([True,2,3.0,[2,3,4.0]]))
