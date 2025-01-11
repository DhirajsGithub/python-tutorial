#for loop

# for i  in range(10):
#     print (f"this is line no: {i}")
#same code below
# for i in range(0, 10):
#     print (f"this is line no: {i}")

# #note i will be increase by 1 and range will be like (x, y) ==> [x,y)

# #sum from 1 to 10:
# num = int(input("enter number "))
# sum = 0
# for i in range (1, num+1):
#     sum = sum + i
#     #sum += i
# print(f"sum is : {sum}")

#Q.
# num = (input("enter a number").strip())
# sum = 0
# for i in range(0, len(num)):
#     sum = sum + int(num[i])
# print (f"sum is {sum}")

# #Q.ask a user for name and count each word in it

# name = input("enter a name: ")
# tempr_var = ""
# for i in range(0, len(name)):
#     if name[i] not in tempr_var :
#         tempr_var += name[i]
#         print(f"{name[i]} : {name.count(name[i])}")


#for loop in string:

# name = "harshit"
# for i in range(0, len(name)):
#     print(name[i])
#usual method to print indexes but python has something else

name = "haeshit"
for element in name:
    print(element)

num = input("enter number")
sum = 0
for i in num:
    sum = sum + int(i)
print(sum)


# nested loops 
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# the pass statement 
# for loops cannot be empty, but if you for
# some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass