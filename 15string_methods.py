#string methods part one
name = "HaRsHIt vaShiSthA"

#1.  len() function
length = len(name)
print(length)

#2.  lower() method
print(name.lower())

#3.  upper() method
print(name.upper())

#4.  title() method
print(name.title())

#5.  count() method
print(name.count("H"))

#6.  centre() method
name = "harshit"
# print(name.centre(11, "*"))          #harshit having length 7 +4stars two of them side by side
print(name.center(len(name)+4, "*"))      #in case we didn't now the length of name
print(name.center(20))                  # by default spaces will be feel. 20 ---> number of characters + remainging will be spaces 
# .ljust(width)       # This method returns a left aligned string of length width.
# .rjust(width)

#7. split() method
print(name.split(" "))      # since it is separated by space
# it will return a list having space

#8 replace() method
l = name.replace("a", "b")
print(l)
print(name.replace("a", "b"))


# str.isalnum # This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
# str.isalpha   # This method checks if all the characters of a string are alphabetical (a-z and A-Z).
# str.isdigit()   #This method checks if all the characters of a string are digits (0-9)
# str.islower()   #This method checks if all the characters of a string are lowercase characters (a-z).

