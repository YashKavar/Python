def person(name,**data):
    print(name)
    for i, j in data.items():
        print(i, "=", j)


person('yash',age=19,city='s.nagar',number=99182746)