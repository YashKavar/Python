
def fibo(n):
    if n<0:
        print("You have enter wrong number.")
    else:
        a=0
        b=1
        if n==1:
            print(a)
        else:
            print(a)
            print(b)
            for e in range(2,n):
                c=a+b
                a=b
                b=c
                print(c)



n=int(input("Enter how many number do yo want to print:"))
fibo(n)