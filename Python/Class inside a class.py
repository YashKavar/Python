
class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.laptop=self.Laptop()

    def show(self):
        print("Name=", self.name, "Roll No.=", self.rollno)
        self.laptop.show()

    class Laptop:

        def __init__(self):
            self.brand='Lenovo'
            self.cpu='i5'
            self.ram=8
        def show(self):
            print("Laptop Brand=", self.brand, "Cpu=", self.cpu, "Ram=", self.ram)


s1=Student('Yash', 6046)
s2=Student('Sagar', 6020)
s1.show()
s2.show()