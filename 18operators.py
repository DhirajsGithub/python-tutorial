#check two conditions at the same time
#and, or
name = "abc"
age = 19
if name == "abc" and age == 19:
    print("condition true")
else :
    print("condition false")

if name == "abc" or age == 18:
    print("condition true")
else :
    print("condition false")

# not    --->	Reverse the result, returns False if the result is true
# is     --->   	Returns True if both variables are the same object
# is not  --->    Returns True if both variables are not the same object
# in   ---->    Returns True if a sequence with the specified value is present in the object
# not in  --->  Returns True if a sequence with the specified value is not present in the object

# &  AND   --->   	Sets each bit to 1 if both bits are 1 
# |  OR    ---->    Sets each bit to 1 if one of two bits is 1
# ^  XOR   ---->    Sets each bit to 1 if only one of two bits is 1
# ~  NOT    ---->   Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	   Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off