
n=int(input("Enter how many number do you want to find:"))
result=0
count=1
for i in range(1,n+1):
    if count%2==0:
        result-=1/i
        count+=1
    else:
        result+=1/i
        count+=1

print(result)