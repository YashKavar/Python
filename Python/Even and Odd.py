from array import *
def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd


lst=array('i',[])
n=int(input("Enter how many number do yo want enter:"))
for i in range(n):
    x=int(input("Enter next number:"))
    lst.append(x)

even,odd=count(lst)
print("even:{} and odd:{}".format(even,odd))