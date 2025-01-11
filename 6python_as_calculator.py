from tkinter import Y
from typing import runtime_checkable


print(2/4)          #it gives deciaml tak- floating point division
print(2//4)         #it will cut fraction wala part- integer division
print(round(2**0.5, 4))  #it will round of root 2 upto 4 decimal places
print(round(22/7, 2))    #it will round of value of pi upto 2 decimal places
 
x = 2+3-(2**2**3) + 10//5
print(x)


#---------------------------------------------------------------------------
# operatos      Description
#   +           addtion
#   -           subtraction
#   *           Multiplication
#   /           Float division
#   //          Integer division
#   %           Modulo,it gives remainder
#   **          Exponent
#------------------------------------------------------------------------------

# Precedence rule :
# --------------------- 
# Operators      |     Precedence and associativity rule
# ------------------------------------------------------------
# Paranthese     |     Highest
# Exponent       |     Right to left
# *, /, //, %    |     left to right
# +, -           |     left to right 

#in groups top to bottom Precedence hai
#in same same group left to right except exponent

# Assignment Operator

#  let p = '='/'+'/'-'/'*'/'/'/'%'/'//'/'**'/'&'/'|'/'^'/'>>'/'<<' = 
# let y = any number
#  x = x p y
# for  x &= y  ----> and gate chalega on binary numbers of x and y after calculating the binary with and the result will be also binary and we get the number value of the resuleted binary
# a = 12 (00001100)
# b = 25  (00011001)
# a & b  --> (00001000) which is binary of 8    ----> AND gate
# similar task for '|'  ----> OR gate

# right shift >> and left shift <<
# considering 5 binary is 101 
# x = 5
# x >> 3   ---> 101 is shifted 3 times to right as 101 | (| --> barries or take is as point) then after shifting by three we left with only 00000.. which is binary of 0
# x << 3   ----> 101 is shifted 3 times to left as  | 101 we have then as 101000   which is binary of 40


# ^  ---->  XOR operator which means  agar 
# similar ke liye 0 opposite ke liye 1
# convert first the given number into binary perform XOR on it's binary then the result will be binary find the value of that binary into a number 
# x    y     x^Y
# 1    1      0
# 1    0      1
# 0    1      1
# 0    0      0