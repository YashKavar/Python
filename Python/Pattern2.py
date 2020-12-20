def pattern(n):
    for i in range(n):
        for j in range(n-i):
            print('# ', end='')
        print()

n=int(input('Enter how many pattern do you want to print'))
pattern(n)
