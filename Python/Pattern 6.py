
n=int(input("Enter number:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
        # k=1
        # while k<=n-i+1:
        #     print(" ",end="")
        #     k+=1
    print("\n")