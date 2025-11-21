# Understanding class creation in Python
# Objective: Create a basic calculator class to perform addition, subtraction, multiplication, and division.
#
# Instructions:
#
# Create a class named BasicCalculator.
#
# Define a constructor that initializes two numbers. Use numbers 10 & 5
#
# Implement methods for:
#
# Addition
#
# Subtraction
#
# Multiplication
#
# Division
#
# Each method should return the result of the operation.
#
# Create an instance of the BasicCalculator class and demonstrate the functionality of each method.
#
# Example Output:
#
# Addition: 10 + 5 = 15
# Subtraction: 10 - 5 = 5
# Multiplication: 10 * 5 = 50
# Division: 10 / 5 = 2.0

#1111111111111
class BasicCalculator:
    def __init__(self,a,b):
        self.first = a
        self.second = b

    def addition(self):
        print("Addition:", self.first + self.second)

    def subtraction(self):
        print("Subtraction:", self.first - self.second)

    def multiplication(self):
        print("Multiplication:", self.first * self.second)

    def division(self):
        print("Division:", self.first / self.second)


obj = BasicCalculator(10, 5)
obj.addition()
obj.subtraction()
obj.multiplication()
obj.division()


print("***************************")
#222222222222222
class BaseCalculator:
    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b
    def addition(self):
        return self.firstnumber + self.secondnumber
    def subtraction(self):
        return self.firstnumber - self.secondnumber
    def multiplication(self):
        return self.firstnumber * self.secondnumber
    def division(self):
        if self.secondnumber > 0:
            return self.firstnumber / self.secondnumber
        else:
            print("Division by zero is not allowed")
            return None
obj = BaseCalculator(10,5)
print("Addition:", obj.addition())
print("Subtraction:", obj.subtraction())
print("Multiplication:", obj.multiplication())
print("Division:", obj.division())



