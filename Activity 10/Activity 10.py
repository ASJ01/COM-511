def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."



print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

op = input("Enter operator (1/2/3/4): ")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

if op == '1':
    result = add(n1, n2)
elif op == '2':
    result = subtract(n1, n2)
elif op == '3':
    result = multiply(n1, n2)
elif op == '4':
    result = divide(n1, n2)
else:
    result = "Invalid operator"

print(f"Result: {result}")