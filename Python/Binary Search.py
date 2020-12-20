from array import *

count=-1
def Search(List,ele):

    l=0
    u=len(List)-1
    while l<=u:
        mid=(l+u)//2
        if List[mid]==ele:
            globals()['count']=mid
            return True
        else:
            if ele<List[mid]:
                u=mid
            else:
                l=mid

List=array('i',[])
n=int(input('Enter How Many Number Do You Want To Enter:'))

for e in range(n):
    x=int(input('Enter Next Number Grater Than Above Number:'))
    List.append(x)

ele=int(input('Enter Which Number Do You Want To Find:'))

if Search(List,ele):
    print('Found at',count+1)
else:
    print('Not Found')