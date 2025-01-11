# define a function which takes one normal parameter and one tuple or list as parameter 
# you have to return a list which return all elements to power normal parameter 

def to_power(num,*args):
    if args :
        num_short_list = [i**num for i in args]
        return num_short_list
    return "hey! mother fucker you didn't pass any args"

nums = [2,3,4,5]
print(to_power(2,*nums))
# or if not want to unpack we can do this
# print(to_power(2,2,3,4,5))


# note how to check if list empty or not !
l = []
if l:              # agar list empty nahi hain toh ye condtion ho jaygi true 
    print("not empty") 
else: 
    print("empty")        #agar list empty hain toh ye condtion ho jayegi true