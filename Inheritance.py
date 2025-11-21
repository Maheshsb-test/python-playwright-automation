#acquiring properties of parent class - inheritance
from OopsDemo1 import Calculator1


class Inheritance(Calculator1):
    Num2 = 200

    def __init__(self):
        Calculator1.__init__(self, 2, 5)

    def getalldata(self):
        return self.Num2 + self.Num + self.Summation()


obj2 = Inheritance()
print(obj2.getalldata())


