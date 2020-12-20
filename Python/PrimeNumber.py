num=int(input('Enter Your Number:'))
for i in range(2,num):
    if num%i==0:
        print('Your Number Is Not Prime')
        break
else:
    print('Your Number Is Prime')