#in keyeord and iteration in dictionary

user_info = {
    'name' : 'harshit',
    'age': 22,
    'fav_movies' : ['coco', 'kimi no na va'],
    'fav_songs' : ['awakening', 'fairy tale']
}

#check if key exist in dictionary :
if 'name' in user_info:           #data type sensitive therfore keys must be in string
    print("present")
else : 
    print("not present")

#check if values exist in dictionary :
if 22 in user_info.values():          #data type sensitvie therfore values must be in there data type format
    print("present")
else : 
    print("not present")

#loops in dictionary :
#keys will be tackle
for i in user_info :
    print(i)


#values method
#tackling values through loop method-1
for i in user_info.values():
    print(i)

#tackling values through loop method-2
for i in user_info:
    print(user_info[i])

#keys
user_info_keys = user_info.keys()
print(user_info_keys)             #print in list form but they are type of dictionary
print(type(user_info_keys))      #type will be as per key types

#values
user_info_values = user_info.values()
print(user_info_values)           #print in list form but they are type of dictionary
print(type(user_info_values))        #type will be as per values type


#item method()  :
user_items = user_info.items()
print(user_items)         # will print TUPLE KI JAISA but in key value pair and type will be dictionary
print(type(user_items))     # dict_items
#[('age', 22), ('fav_songs', ['awakening', 'fairy tale']), ('name', 'harshit'), ('fav_movies', ['coco', 'kimi no na va'])]

for i in user_items:
    print(i)
#tuples unpacking
for i, j in user_items:
    print("key is {} value is {}".format(i,j))