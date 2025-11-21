# Average Calculator
# Objective: Calculate the average of three numbers.
#
# Instructions:
#
# Create a function called CalculateAverage that takes three parameters: num1, num2, and num3.
#
# Use the numbers 10,20,30 as input to functions
#
# The function should return the average of these three numbers.
#
# Expected Output:
#
# The average of 10, 20, and 30 is 20.0

class Twelve:
    def CalculateAverage(self, num1, num2, num3):
        self.n1 = num1
        self.n2 = num2
        self.n3 = num3
        num4 = self.n1 + self.n2 + self.n3
        Average = num4 / 3
        print("The average of 10, 20, and 30 is", Average)

obj = Twelve()
obj.CalculateAverage(10, 20, 30)



print("*****************************")
class Twelve:
    def CalculateAverage(num1, num2, num3):
        return (num1 + num2 + num3) / 3

    # Calling the function with different sets of numbers
    average1 = CalculateAverage(10, 20, 30)
    print("The average of 10, 20, and 30 is", average1)