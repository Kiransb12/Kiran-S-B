# Problem-1.py
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Error: Division by zero"

calc = Calculator()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == '+':
    print(calc.add(a, b))
elif op == '-':
    print(calc.subtract(a, b))
elif op == '*':
    print(calc.multiply(a, b))
elif op == '/':
    print(calc.divide(a, b))
else:
    print("Invalid operation")
