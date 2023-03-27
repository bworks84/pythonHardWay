def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b


def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b


print("Let's do some math with just functions")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}.")

# A puzzle for the extra credit, type it in anyway.
print("here's a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# 4 add(age, -4426)
# 3 subtract(height, 4500) = 74 - 4500
# 2 multiply(180, 25) = 4500
# 1 divide(50, 2) = 25

print(f"That becomes: ", {what}, "Can you do it by hand?")
