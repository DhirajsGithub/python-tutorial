# Text Type:    	str
# Numeric Types: 	int, float,complex
# Sequence Types:	list, tuple,range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray,memoryview


# use some of the non use variables 
from cmath import log10
from pprint import pprint


x = 1j          # complex data type
print(x)
print(2+x)      # not error, it's real + imaginary part
l = 4
l1 = complex(l)
print(type(l1))                     # <class 'complex'>

y1 = range (6)      # range data type
print(y1)           # output ---> range(0,6)

y = list(range(6))
print(y)            # output ----> [0, 1, 2, 3, 4, 5]

z = frozenset({"apple", "mango", "banana"})
print(z)
# Frozen sets are a native data type in Python that have the qualities of sets 
# — including class methods 
# — but are immutable like tuples. To use a frozen set, call the function frozenset() and pass an iterable as the argument. 
# If you pass a set to the function, it will return the same set, which is now immutable.

m = b"Helllow"
# n = c"Helllow"        # error
print(m)                # output (b'Hellow')
print(type(m))          # <class 'bytes'>

n = bytearray(5)
print(n)
# bytearray() method returns a bytearray object which is an array of given bytes. 
# It gives a mutable sequence of integers in the range 0 <= x < 256. 
# Returns: Returns an array of bytes of the given size. source parameter can be used to initialize the array in few different ways.
# the main difference between byte and bytearray is that byte are immutable whereas bytearray is muttable

print("----------memory view bytearray----------")

p = memoryview(bytearray(8))
p1 = memoryview(bytes(5))
print(p)
print("-------memory view byte------")
print(p1)
# memoryview objects allow Python code to access the internal data of an object that supports the buffer protocol without copying.
# The memoryview() function allows direct read and write access to an object's byte-oriented data without needing to copy it first.



