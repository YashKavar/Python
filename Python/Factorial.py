def fact(n):

    f = 1
    for i in range(1, n+1):
        f = f*i
    return f
x=int(input("Enter which number of factorial do you want to find:"))

result=fact(x)
print(result)