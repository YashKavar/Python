
f=open('Data','r')

f2=open('Data 2','w')

for data in f:
    f2.write(data)

f3=open('IMG20191205195120.jpg','rb')
f4=open('My Image.jpg','wb')

for i in f3:
    f4.write(i)