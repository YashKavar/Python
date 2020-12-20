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
                if c<n:
                    print(c)



n=int(input("Enter which number do you have to print at most:"))
fibo(n)