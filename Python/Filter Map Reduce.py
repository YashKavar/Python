from functools import reduce


num=[1, 2, 5, 8, 3, 9, 6, 2, 8, 5, 9]
evens=list(filter(lambda n: n%2==0, num))
print(evens)
double=list(map(lambda n: n*2, evens))
print(double)
sum=reduce(lambda a,b: a+b, double)
print(sum)