# more about function
def square (a):
    return a**2

s = square
print(s(7))
print(square(7))

print(s.__name__)
print(square.__name__)

print(s)               #both are store in same location in memory
print(square)
