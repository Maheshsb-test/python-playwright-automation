#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#The constructor is a method that is called when an object is created.
#This method is defined in the class and can be used to initialize basic variables.


class Calculator:
    Num = 100   # class varibales


    def getdata(self):
        print("I am executing method in a class")

obj = Calculator()
obj.getdata()
print(obj.Num)


print("*******************")


#constructor
class Calculator:
    Num = 100   # class varibales
    def __init__(self):
        print("i am called automatically once object is created")

    def getdata(self):
        print("I am executing method in a class")

obj = Calculator()
obj.getdata()
print(obj.Num)


print("*********FF**********")


class Calculator1:
    Num=100
    def __init__(self,a,b):
        self.FirstNumber=a
        self.SecondNumber=b
        print("i am called automatically once object is created")

    def getdata(self):
        print("I am executing method in a class")

    def Summation(self):
        return self.FirstNumber + self.SecondNumber + Calculator.Num

obj = Calculator(2,3)
obj.getdata()
print(obj.Summation())

obj1 = Calculator(4,5)
obj1.getdata()
print(obj1.Summation())










