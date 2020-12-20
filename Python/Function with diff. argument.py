def person(name,age=19):
    print(name)
    print(age)

def add(*b):
    x=0
    for i in b:
        x=x+i

    print(x)


# position
person('yash',18)
# keyword
person(age=20,name='yash')
# defult
person('yash')
# argument length
add(5,6,7,9,4)