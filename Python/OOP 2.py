
class Computer:

    def __init__(self, cpu, ram):
        self.a=cpu
        self.b=ram

    def config(self):
        print("Cpu=",self.a, "Ram=",self.b)


com1=Computer('i5', 16)
com2=Computer('Ryzen3', 8)

com1.config()
com2.config()