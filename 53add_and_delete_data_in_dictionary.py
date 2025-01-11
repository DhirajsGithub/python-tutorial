#add and delete data:
user_info = {
    'name' : 'harshit',
    'age': 22,
    'fav_movies' : ['coco', 'kimi no na va'],
    'fav_songs' : ['awakening', 'fairy tale']
}

#add data in dictionay
user_info['hobbies']  = ['guitar', 'sleeping']
print(user_info)

#pop method
popped_list = user_info.pop('fav_songs')
# #argument as a key dalna jaruri hain list ki tarah ye last se nahi nikalega
# print("popped item is {}".format(popped_list))
# print(user_info)
# print(type(popped_list))
# print(type(user_info))

#popitem method
popped_item = user_info.popitem()
#it will remove random tuple
print(popped_item)
print(type(popped_item))   #type will be tuple
print(user_info)