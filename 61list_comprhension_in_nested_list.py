#listed comprhension in nested list

#generate this
# example = [[1,2,3], [1,2,3], [1,2,3]]

nested_comp = [[i for i in range(1,4)] for j in range(5,10)]
print(nested_comp)
nested_comp2 = [[i,j] for i in range(1,4) for j in range(1,4)]
print(nested_comp2)

nested_list = []

for i in range(1,4):
    sub_list = []
    for j in range(1,4):
        sub_list.append(i)
        
    nested_list.append(sub_list)
print(nested_list)

print("---------nested of nested -------------")
li = [[i,j,k] for i in range(0,2) for j in range(3) for k in range(2) if (i+j+k) !=0]
print(li)