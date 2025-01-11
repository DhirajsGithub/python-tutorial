#string indexing
language = "python"

#  p  y  t  h  o  n              #position/indexing 0 se start hoti hai agar start se dekhe toh
#  0  1  2  3  4  5
#  -6 -5 -4 -3 -2 -1            #position/indexing -1 se start hoti hai agar last se dekhe toh

print(language[4])
print(language[-2])

#strings are immutable and they are iterable
#matlab apne original string ko nahi badal sakte
string = "string"
new_string = string.replace("t", "T")         #is variable ne nahi string bana li aur usme change kiya
print(new_string)
print(string)

#but we can change the string by assigning new variable
name = "harsh"
# name = name + "it" #Or
name += "it"
print(name)

# NOTE list object have no attribute like .replace 