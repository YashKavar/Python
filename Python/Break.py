av = 6
x = int(input('Enter how much candy do you want'))
i = 1
while i <= x:
    if i>av:
        print('Out of stock')
        break
    print('candy')
    i += 1
print('Bye')
