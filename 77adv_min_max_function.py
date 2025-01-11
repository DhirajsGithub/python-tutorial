# advance of min() and max() function

# numbers = [3.4,667,23,69,1,0]
# print(min(numbers))

names = ["Harshit", "abc", "a"]
# print out the name with max/min length
def func (name):
    return len(name)

# print(max(arg1, arg2))   #syntax for max/min function   note: arg1 must be iterable and arg2 must be function
print(max(names, key = func))
print(min(names, key = func))

# with lambda function : 
print(max(names, key = lambda name: len(name)))

students = [
    {'name': "harshit", 'score': 90, 'age': 22},
    {'name': "harshal", 'score': 60, 'age': 20},
    {'name': "nishant", 'score': 70, 'age': 18}
]
# find the person having max score in the given list
print(max(students, key = lambda item : item.get('score')))    #dictionary will be print out
print(min(students, key = lambda item : item.get('score'))['name'])

students2 = {
    "mohit": {'score': 90, 'age': 22},
    "naresh": {'score': 60, 'age': 20},
    "nilesh": {'score': 70, 'age': 18}
}
# find the person having max score in the given dictionary of dictionary
# def func_2 (item):
#     return (students2[item])['score']       #acche se dekho bhai key value pair se value ko access keya fir bad main usi ke under key value ko access kiya

# print(max(students2, key = func_2))

print(max(students2, key = lambda item : students2[item]['score']))