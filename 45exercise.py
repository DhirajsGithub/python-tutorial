#define a function which will take list containing numbers as input
#and return list containing square of every elements

# numbers = [1,2,3,4,5,6,7,8,9,10]

# def square_list(num):
#     squares = []
#     for element in num:
#         mul = element*element
#         squares.append(mul)
#     return squares

# print(square_list(numbers))


# #define a function which will take list as a argument and this fuction will return a reversed list
# #use only append() and pop() method
# def reverse_funct(myinput):
#     myoutput = []
#     for i in range(0,len(myinput)):
#         popped = myinput.pop()
#         myoutput.append(popped)
#     return myoutput
    
# print(reverse_funct([1,2,3]))


#define a function that take list of words as argument and return list with reverse of every element in that list

# def reverse_list(myinput):
#     myoutput = []
#     for element in myinput:
#         myoutput.append(element[::-1])
#     return myoutput

# print(reverse_list(['abc', 'bcd']))
#Or
# def reverse_list(myinput):
#     myoutput = []
#     for i in range(0, len(myinput)):
#         myoutput.append(myinput[i][::-1])
#     return myoutput

# print(reverse_list(['abc', 'bcd']))

#define a function which filters odd even in two lists inside a list
def filterOddEven (list):
    even = []
    odd = []   
    for element in list:
        if element%2 == 0:
            even.append(element)
        else:
            odd.append(element)
    evenOdd =[even, odd]
    return evenOdd

print(filterOddEven([1,2,3,4,5,6,7,9]))


#define a function which takes two parameters as a list and returns a list which conatins comman elements of both parametric list
# def filterComman (list_1, list_2):
#     comman = []
#     for i in range (0, len(list_1)):
#         if list_1[i] == list_2[i]:
#             comman.append(list_1[i])
#     return comman

# print(filterComman([1,2,3], [1,2,3,5,6,7]))
def filterComman (list_1, list_2):
    comman = []
    for element_1 in list_1: 
         for element_2 in list_2:
             if element_1 == element_2:
                 comman.append(element_1)
    return comman

print(filterComman([1,2,3], [9,2,3,5,6,7]))
# ye method best hain, indexing walen ke case main ho ye raha tha ki woh index no pr agar comman hain tabhi same dikha raha tha 