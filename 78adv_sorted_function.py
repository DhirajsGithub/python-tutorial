#advance sorted function
fruits = ['grapes', 'mangp', 'apple']
fruits.sort()
print(fruits)

fruits2 = ('grapes', 'mangp', 'apple')
# fruits2.sort()             # since tuples are immutable hence can't change the original one
# print(fruits2)     
print(sorted(fruits2))        #but can store the change and then print out

fruits3 = {'grapes', 'mangp', 'apple'}
# fruits3.sort()             # since sets are immutable hence can't change the original one
# print(fruits3)     
print(sorted(fruits3))        #but can store the change and then print out


guitars = [
    {'model1': 'yamaha', 'price' : 5000},
    {'model2': 'faith', 'price' : 2000},
    {'model3': 'taylor', 'price' : 9000}
]
#sort above guitars according to their prices
# def func (item):
#     return item['price']

# print(sorted(guitars, key = func))

# sorted_guitars = sorted(guitars, key = lambda item: item.get('price'))
# print(sorted_guitars)

sorted_guitars_rev = sorted(guitars, key = lambda item: item.get('price'), reverse=True)
print(sorted_guitars_rev)