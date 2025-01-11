#output : Line A \n Line B
print("Line A \\n Line B")        #--------1
#output : \" \'
print (" \\\" \\\'")

#very important note: print(r"something \ ")  will print something \
print(r"LineA \n Lineb")         # is similar to code 1
#any escape sequence can print simply by adding r at the beginning