class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
class BasicCalculator(Calculator):
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b
class AdvancedCalculator(BasicCalculator):
    def square(self, a):
        return a * a
    def power(self, a, b):
        return a ** b
calculator = AdvancedCalculator()
print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))
print("Multiplication:", calculator.multiply(10, 5))
print("Division:", calculator.divide(10, 5))
print("Square:", calculator.square(10))
print("Power:", calculator.power(2, 3))