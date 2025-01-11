#deifine a function which takes input from user and returns it's last chatacter
def last_char (a):                 # here a is called parameter
    last = a[len(a)-1]
    return last

something = input("enter something i don't know what bu anything man").strip()
print(last_char(something))             # here "someting" is called argument
#note: only pass string if want to pass number then convert it into string kyun yaise indexing ka kaam apn sirf string main hi kar sakte hai!


#define a function which reutrns if input is odd or even
# def odd_even (a):
#     if a%2==0 :
#         return "even"      #print("even") bhi likh sakte the no problem toh nich print likhne ki jarurat nahi rahti
#     else :
#         return "odd"  
# num = int(input("enter a number: ").strip())
# print(odd_even(num))

#above code in small manner
# def odd_even (a):
#     if a%2==0 :
#         return "even"
#     return "odd" 

# num = int(input("enter a number: ").strip())
# print(odd_even(num))
# #agar if ki condition nahi chali toh if walen bracket se bahar nikal jate hain toh apn return"odd" pr aa jayege

#above code with boolean
# def is_even (a):
#     if a%2 == 0:
#         return True
#     return False

# print(is_even(9))

# #above code thoda aur short
# def is_even (a):
#     return a%2 ==0 

# print(is_even(5))
# #it will automatically check reurn boolean value

#we can also define a function without parameter
def song():
    return "happy birthday song"

print(song())