#update method
user_info = {
    'name' : 'harshit',
    'age': 22,
    'fav_movies' : ['coco', 'kimi no na va'],
    'fav_songs' : ['awakening', 'fairy tale']
}

more_info = {
    'state' : 'haryana',
    'hobbies' : ['sleeping', 'coding', 'reading'],
    'name' : 'mohit'
}
user_info.update(more_info)
print(user_info)
#IF KEYS ARE REPEATING THEN IT WILL UPDATE IT'S VALUE

user_info.update({})
#empty dictionary won't update the previous one empty. data in previous dictionary waisa ka waisa rahega
print(user_info)

# set default() method
x = user_info.setdefault("verganity", "yes")
print(x)
print(user_info)


