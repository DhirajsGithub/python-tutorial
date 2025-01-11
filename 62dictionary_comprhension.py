#dictionary comprhension
# square = {1:1, 2:4, 3:9, 4:16}
# square = {}
# for i in range(1,5):
#     square[i] = i**2

# print(square)
# square_obj_short = {i:i**2 for i in range(1,11)}
square_obj_short = {f"square of {i} is" : i**2 for i in range(1,11)}
# print((square_obj_short))
# to print in vertical 
for i,j in square_obj_short.items():
    print(f"{i} : {j}")

#word counter

name = "harshit"
# count = {}
# for i in name :
#     count[i] = name.count(i)
# print(count)

count_short = {f"char is {char}": name.count(char) for char in name}
# print(count_short)
for i,j in count_short.items():
    print(f"{i} : {j}")














    