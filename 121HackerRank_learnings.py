# M-1
# import sys
# l = []
# for line in sys.stdin:
#     l.append(line)

# M-2
# Input Format
# A single line containing the space separated values of  N and M.
# N, M= input().split(" ")
# N = int(N)
# M = int(M)

import imp


l = ["abc", 'dfvf', "df"]    # every item must be a string
p = " ".join(l)
p = "".join(l)
print(p)


# to print all items in a line with parenthesis only to i and j
# l1 = ['1', '2']
# l2 = ['3','6']
# for i in l1:
#     for j in l2:
#         print((int(i),int(j)), end=" ")


# to get the line by line inputs
# for line in sys.stdin:
#     shoe_size_price.append(line)

# print(shoe_size_price)
import sys
l = list(sys.stdin)
print(l)




import cmath
import math
c = input()
# print(c)
# print(c.real)
# print(c.imag)

# r = c.real
# i = c.imag
# abs = math.sqrt(r**2+i**2)
# phase = math.atan(i/r)

# if (i<0 and r>0 ) or (i>0 and r<0):
#     phase = phase*-1

# print(abs)
# print(phase)

complex(c)     # ----> take real and imaginary part
print(abs(complex(c)))         # absolute value 
print(cmath.phase(complex(c)))       # take care of sign of taninverse