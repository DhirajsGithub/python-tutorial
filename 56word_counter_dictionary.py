# word counter
# dic = {'name': 'Harshit', 'age': 22, 'age' : 34}
# print(dic)
# we know that same keys can't be print in dicionary hence it become easy to count letter of a word
# def word_counter(name):
#     counter = {}
#     for char in name :
#         counter[char] = name.count(char)
#     return counter

# print(word_counter("harshal"))



#define a function that takes a number(n)
#return a dictionary containg cube of numbers from 1 to n

# def cubeFinder(n):
#     dic = {}
#     for i in range(1,n+1):
#         dic[i] = i**3
#     return dic 

# print(cubeFinder(4))

#store data in dictionary form user
#and print the data in vertical form not like horzontally
users = {}
name = input("enter you name")
age = input("enter you age")
fav_movies = input("enter you favourite movies comma seperated").split(",")
#default list main store ho jayege

users['name'] = name
users['age'] = age
users['fav_movies'] = fav_movies

# print(users)
for key, value in users.items():
    print(f"{key}: {value}")




