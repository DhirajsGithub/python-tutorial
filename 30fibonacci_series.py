#fibonacci series
# 0 1 1 2 3 5 8 13 21 34
def fibonacci_series (num):
    a = 0
    b = 1
    if num==1 :
        print(a)
    elif num==2 :
        print (a,b)
    else:
        print(a, b, end =" ")
        for i in range (num-2):
            c = a+b
            a = b
            b = c
            print ( b, end =" ")           #note method to print in a line

fibonacci_series(10)

# 0 1 1 2 3 5 8 13 21 34