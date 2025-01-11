# dictionary comprhension with if-else statement
# dictionary = {}
# for i in range(1,6):
#     if i%2 ==0:
#         dictionary[i] = "even"
#     else: 
#         dictionary[i] = "odd"
# print(dictionary)

dictionary_short = {i:"even" if i%2==0 else "odd" for i in range(1,6)}
for i , j in dictionary_short.items():
    print(f"{i} : {j}")