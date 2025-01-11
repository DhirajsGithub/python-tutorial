#strip method()
name = "   Har     shit    "
dots = "............"
print(name + dots)
print(name.lstrip() + dots)            #left side wali space remove hogi not affecting spaces between two strings
print(name.rstrip() + dots)            #right side wali space remove hogi not affecting spaces between two strings
print(name.strip() + dots)             #left and right side wali space remove hogi not affecting spaces between two strings
print(name.replace(" ", "") + dots)    #it will remove spaces between string 

#replace method()
string = "she is beautiful and she is good dancer"
print(string.replace("is", "was"))           #all is's will be replace by was's
print(string.replace("is","was",1))          #it will replace only first is as mention only 1 (it's not a positon it is number of is)
print(string)                                # original string ko kuch huae hi nahi 

# print(string.find("is"))                   #it will find first is and count from 0 letters count karega + spaces bhi
# print(string.find("is", 5))                #since hame pata hai ki pahale is ki positon 4 hai toh apn dusre is ke position ke liye 5 se start karege

#like a pro
is_post1 = string.find("is")                  #index number will be shown of i in string
is_post2 = string.find("is", is_post1+1)
print(is_post2)


