
class Top:

    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=15:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration


values=Top()
print(values.__next__())

for i in values:
    print(i)