
# from string import ascii_lowercase
# apl_list = ascii_lowercase
# print(apl_list)
# print(list(apl_list))

# # print(type(ascii_lowercase))
# c = "d"
# li = [i for i in c]
# print(li)
# i = "abc jkfdj ljkds fdfsd"
# l = i.split(" ")
# print(l)
# from operator import index, truediv
# from re import X
# from tkinter.tix import Tree
# from traceback import print_tb


# k = 5
# dict = {

# }

# for i in range(5):
#     dict["t"+str(i)] = i

# print(dict)
# for i in dict.keys():
#     print(i)
# X
# for i in range(1,int(5+1)): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     # print (int(lambda a : (i-a+1) for a in range(1,i+1)))

#     x = list(range(5))
# # print(i-j+1, )
# print(list(i for i in range(5)))

# for i in range(1, 5):
#     x = list((map(lambda a : i-a+2, list(range(i+1,1,-1)))))

# x = (2,)
# print(type(x))

# l1 = {1,3,5,7}
# l2 = [2,4,6,8]

# # for i in l1:
# #     print(index(i))
# # print(True - False)

# from re import L


# l=['asdf','sf2ek','sf5bskfg']
# for i in l:
#     if type(i)==str:
#         print(i)
#         continuel
# l = [1,2,3,4,5,6,7,8]
# for i in l:
#     print(i)
#     l= l[0:-1]
#     print(l)
# print(l)

# print(l[1:3])

import math


# def main(a, b):
#     if func(a) == 0:
#         return a
#     elif func(b) == 0:
#         return b
#     elif func(a)*func(b) > 0:
#         return "root not exist between the interval"
#     else:
#         return IVT(a, b)


# def IVT(a, b):
#     ass = -1
#     while (a < b):
#         mid = (a+b)/2
#         if abs(func(mid)) < 0.0001:
#             return mid
#         if func(a)*func(mid) <= 0:
#             b = mid
#         else:
#             a = mid
#     return a


# def func(x):
#     val = math.sin(2*x)*math.exp(x-4)
#     return val


# root = main(1, 2)
# print(root)
# print(func(1.6170))


# % Question 1
# % equatino = 6x^6 + 4x^5 + 5x^4 - 10x^3 + 3x^2 -9x -89
# % solve for x = 4
# % assuming all degrees are present
# % coeff = [6, 4, 5, -10, 3, -9, -89]
# coeff = [3, 9, 4, -4];
# degree = length(coeff)-1
# pp = solvePoly(coeff, 1, degree)

# % Question 2
# a = 1;
# b = 2;
# re = main(1, 2)

# function temporary = tempor()
#     temporary = 2;
# end
# %----------------- question 2 function --------------------------
# % as a parameter the function solvePoly will take a matrix containgn all
# % the coefficients of the equation
# % matrix will contain elements as descending order of their power
# % function takes a matrix m and to solve a equation for 'a' and degree of
# % the equation
# function answer = solvePoly(m, a, degree)
#     answer = 0;
#     if degree <= 2
#         d = degree;
#         for c = 1 : degree
#             answer = answer + m(c)*(a^d);
#             d = d-1;
#         end
#     else
#         answer = m(1)*a + m(2);
#         for c = 3: degree+1
#             answer = answer*a + m(c);
#         end

#     end

# end

# %----------------- question 1 functions --------------------------
# % a, b are interval to find the root between
# function result = main(a, b)
#     if func(a) == 0
#         result = a;
#     elseif func(b) == 0
#         result = b;
#     elseif func(a)*func(b) > 0
#         result = "root not exist between given interval";
#     else
#         result = IVT(a, b);
#     end
# end

# function aa = IVT(a, b)
#     aa = -1;
#     while(a < b)
#         mid = (a+b)/2;
#         if abs(func(mid)) < 0.00001
#             aa = mid;
#             break;
#         elseif func(a)*func(mid) <=0
#             b = mid;
#         else
#             a = mid;
#         end
#     end
# end

# function val = func(x)
#     val = sin(2*x)*exp(x-4);
# end


# def gaussEli(matr):
#     for k in range(0, len(matr)-1):     # for len(matr)-k X len(matr)-k matrix
#         for i in range(k+1, len(matr)):     # selecting propert mi
#             mi = matr[i][k]/matr[k][k]
#             for j in range(k, len(matr)):       # reducing the row
#                 matr[i][j] = matr[i][j] - matr[k][j]*mi


# matr = [[2, 4, 5], [4, 5, 6], [7, 2, 3]]
# gaussEli(matr)
# print(matr)
