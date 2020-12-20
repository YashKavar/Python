
class car():

    whell=4
    def __init__(self):
        self.mil=10
        self.brand="BMW"


c1=car()
c2=car()
car.whell=5

print(c1.brand, c1.mil, c1.whell)
print(c2.brand, c2.mil, c2.whell)