
n=int(input("Enter number:"))
for i in range(1,n+1):
    for j in range(i-1):
        print("  ",end="")
    for j in range(n-i+1):
        print("* ",end="")
    print("\n")