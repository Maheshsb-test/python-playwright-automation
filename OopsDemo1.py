class Calculator1:
    Num=100
    def __init__(self,a,b):
        self.FirstNumber=a
        self.SecondNumber=b
        print("i am called automatically once object is created")

    def getdata(self):
        print("I am executing method in a class")

    def Summation(self):
        return self.FirstNumber + self.SecondNumber + Calculator1.Num

obj = Calculator1(2,3)
obj.getdata()
print(obj.Summation())

obj1 = Calculator1(4,5)
obj1.getdata()
print(obj1.Summation())