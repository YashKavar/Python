from array import *

arr=array('i', [])

n=int(input("Enter how many number do you want to enter:"))

for i in range(n):
    x=int(input("Enter next element:"))
    arr.append(x)

s=int(input("Enter element which you can search:"))

# with the manual search
k=0
for e in arr:
    if e==s:
        print("Your element are founded successfully at index:")
        print(k)
        break
    k+=1
else:
    print("Your element are not found")
# with the use of inbuilt function
print(arr.index(s))
