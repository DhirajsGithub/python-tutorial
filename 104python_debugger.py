import pdb     # import python debugger module
# module - python file contains usefull classes and functions wrote by developers 

# debugging is the process of finding and resolving defects or problems within a computer program that prevent
# correct operation of computer software or a system

# why debugging ?
# 1.) our programme is not running and causing unexpected errors.
# 2.) our programme is working fine but not working in same way we want 

# steps for debugging
# 1.) set trace 
# 2.) execute code line by line


pdb.set_trace()
name = input("enter your name: ")
age = input("input your age: ")

print(f"your name is {name} your age is {age}")

age2 = age + 5

print(f"after five year you will become {age2} years old")

# when we set pdb.set_trace() and we run our code it will then execute line by line 
# by writing 'l' we will get to know where our code is at
# by writing 'n' we then can run the code at that line
# when the lines are executed we can also check if the variables exist or not
# we can apply from anywhere pdb.set_trace() where we think that bug starts

# by pressing 'c' code will be executed normally

# by pressing 'q' code will be quite
