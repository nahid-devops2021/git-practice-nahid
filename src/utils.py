# Add
def add(a, b):
    return a + b

# Subtract
def subtract(a, b):
    return a - b

# Multipling
def multiply(a, b):
    return a * b

# Error handling
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Invalid Divide !!!"