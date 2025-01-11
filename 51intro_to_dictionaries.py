# dictionaries intro
# we use dictionaries because of limitations of list, lists are not enough to store real world data

#example
user = ['harshit', 24, ['kabir sing', 'peter rabbit'], ['13 resons why', 'you']]
# this list contains username, age, favmovie, favserires
#you can do this but this is not a good method to store all such data

#dictionaries are unordered collection of data in key: value pair
#dictionaries are mutable

#creating a dictionary
#generally it has a key and it's value in pair
#first method
user = {'name': 'Harshit', 'age': 19}
print(user)
print(type(user))

#second method
user1 = dict(name = 'harshit', age = 22)

#keys in dictionary are always in string or integer or tuple values can be of any data structure

#accesing dictionary
#note there is no indexing because of unoredered collections of data.
print(user['name'])
print(user1['age'])

#we can store any type of data in dictionary
user_info = {
    'name' : 'harshit',
    'age' : 22,
    'fav_song' : ['heaven', 'dariya', 'karvaa'],
    'fav_movies' : ['kabir sing','rabit']
} 
print(user_info)

#adding data to empty dictionary
user_info2 = {}
user_info2['name'] = 'mohit'
user_info2['varginity'] = 'maintain'
user_info2['age'] = 22
print(user_info2)