from array import *

count=0
def Search(List,ele):

    for i in range(len(List)):
        global count
        if List[i]==ele:
            return True
        count+=1
    else:
        return False

List=array('i',[])
n=int(input('Enter How Many Number Do You Want To Enter:'))

for e in range(n):
    x=int(input('Enter Next Number:'))
    List.append(x)

ele=int(input('Enter Which Number Do You Want To Find:'))

if Search(List,ele):
    print('Found at',count+1)
else:
    print('Not Found')