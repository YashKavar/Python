from array import *

val=array('i', [5,6,3,8,11])
newArray=array(val.typecode, (a*a for a in val))

for i in newArray:
    print(i)