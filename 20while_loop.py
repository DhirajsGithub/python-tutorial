#while loop

# i = 1
# while i<=10 :
#     print("Hellow")
#     i = i+1

# print("condition falls at", i)

#summation using while loop:

# sum = 0
# i = 1
# while i <= 10:
#     sum = sum + i
#     i= i+1

# print("total is equal "+ str(sum))

# #Q.take input a number from user and print out the summation of all the digit in that number
# num = (input("enter a number").strip())
# length = len(num)
# # num = int(num)
# print(num)
# print(length)
# print(num[1])

# sum = 0
# i = 0
# while i< length:
#     sum = sum + int(num[i])
#     #sum += int(num[i])
#     i = i+1
# print(sum) 
# #kya sikhe indexing apn integer ki kar hi nahi sakte woh sirf string and arrays ke liye hoti hain
# #algorithm = (method to solve problem in human language)


#Q.ask a user for name and count each word in it
name = input("enter your name")

i=0 
temp_var = ""
while i < len(name):
    if name[i] not in temp_var :
        temp_var = temp_var + name[i]
        print(f"{name[i]}: {name.count(name[i])}")
    i += 1

#note we use if in statement on that contrary we have if not in statement 

