# 1. Arithmetic Operators
a = 10
b = 5

print("Arithmetic Operators:")
print(f"a + b = {a + b}")  # Addition
print(f"a - b = {a - b}")  # Subtraction
print(f"a * b = {a * b}")  # Multiplication
print(f"a / b = {a / b}")  # Division
print(f"a // b = {a // b}")  # Floor Division
print(f"a % b = {a % b}")  # Modulus
print(f"a ** b = {a ** b}")  # Exponentiation
print()

# 2. Assignment Operators
x = 10
print("Assignment Operators:")
x += 5  # x = x + 5
print(f"x += 5 -> {x}")
x -= 3  # x = x - 3
print(f"x -= 3 -> {x}")
x *= 2  # x = x * 2
print(f"x *= 2 -> {x}")
x /= 4  # x = x / 4
print(f"x /= 4 -> {x}")
x //= 3  # x = x // 3
print(f"x //= 3 -> {x}")
x %= 2  # x = x % 2
print(f"x %= 2 -> {x}")
x **= 2  # x = x ** 2
print(f"x **= 2 -> {x}")
print()

# 3. Comparison Operators
a = 10
b = 5
c = 10

print("Comparison Operators:")
print(f"a == b -> {a == b}")  # Equal to
print(f"a != b -> {a != b}")  # Not equal to
print(f"a > b -> {a > b}")    # Greater than
print(f"a < b -> {a < b}")    # Less than
print(f"a >= c -> {a >= c}")  # Greater than or equal to
print(f"a <= b -> {a <= b}")  # Less than or equal to
print()

# 4. Logical Operators
x = True
y = False

print("Logical Operators:")
print(f"x and y -> {x and y}")  # Logical AND
print(f"x or y -> {x or y}")    # Logical OR
print(f"not x -> {not x}")      # Logical NOT
print()

# 5. Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("Identity Operators:")
print(f"x is y -> {x is y}")  # Identical (same object in memory)
print(f"x is z -> {x is z}")  # Identical (same object in memory)
print(f"x is not y -> {x is not y}")  # Not identical
print(f"x is not z -> {x is not z}")  # Not identical
print()

# 6. Membership Operators
list1 = [1, 2, 3, 4, 5]

print("Membership Operators:")
print(f"3 in list1 -> {3 in list1}")  # Element present in list
print(f"6 not in list1 -> {6 not in list1}")  # Element not present in list
print()

# 7. Bitwise Operators
a = 60  # 60 = 0011 1100 in binary
b = 13  # 13 = 0000 1101 in binary

print("Bitwise Operators:")
print(f"a & b -> {a & b}")  # Bitwise AND
print(f"a | b -> {a | b}")  # Bitwise OR
print(f"a ^ b -> {a ^ b}")  # Bitwise XOR
print(f"~a -> {~a}")        # Bitwise NOT
print(f"a << 2 -> {a << 2}")  # Bitwise Left Shift
print(f"a >> 2 -> {a >> 2}")  # Bitwise Right Shift
