#set comprhension
# s = {"test string",}
# for i in range(1,11):
#     s.add(i**2)

# print(s)

s = {i**2 for i in range(1,11)}
print(s)