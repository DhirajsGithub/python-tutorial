def square(a):
    return a**2

l = [1,2,3,4,5]

#1
# print(list(map(square, l)))

#2
# def my_map (func, l):
#     square_l = []
#     for item in l:
#         square_l.append(func(item))
    
#     return square_l

# print(my_map(square, l))

#3
# print(list(map(lambda a : a**2, l)))

#4
def my_map (func, l):
    square_l = [func(a) for a in l]
    return square_l

print(my_map(square, l))
                        
