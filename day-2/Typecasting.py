# Typecasting in Python

"""
Typecasting is the process of converting the value of one data type to another.
It allows programmers to perform operations on variables of different types.
Common conversions involve converting between strings, integers, floats, and booleans.
Python provides both implicit and explicit typecasting mechanisms.
"""

# Built-in casting functions: str(), int(), float(), bool()

# Example to show a TypeError when incompatible types are used
a = "Aisha"
# a += 1  # ❌ This will raise an error: TypeError because you can't add int to string

# ---------------------------------------------
# Variables of different data types
name = "Aisha"
age = 23
gpa = 3.99
is_girl = True

# Checking types using the type() function
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(gpa))     # <class 'float'>
print(type(is_girl)) # <class 'bool'>

# ---------------------------------------------
# Explicit Typecasting: Manual conversion using functions like str(), int(), float(), bool()

# Convert int to string
age = str(age)
age += "1"  # String concatenation
print(age)  # Output: "231"

# Convert float to int (decimal part will be removed)
gpa = int(gpa)
print(gpa)  # Output: 3

# Convert boolean to string
is_girl = str(is_girl)
print(is_girl)  # Output: "True"

# ---------------------------------------------
# Types of Typecasting in Python

# 1. Implicit Typecasting
"""
Python automatically converts one data type to another when it makes sense.
This usually happens when performing operations on mixed types (e.g., int + float).
"""
x = 10       # int
y = 3.5      # float
result = x + y  # int + float → float
print(result)       # Output: 13.5
print(type(result)) # <class 'float'>

# 2. Explicit Typecasting
"""
Manual conversion of one data type to another using casting functions.
This is required when automatic conversion is not provided by Python.
"""
x = "100"
x = int(x)  # Convert string to int
print(x + 20)  # Output: 120

# Boolean conversions
y = 0
print(bool(y))  # Output: False (0 is considered False)

z = 1
print(bool(z))  # Output: True (non-zero is True)

# 3. Constructor Typecasting
"""
Using constructors of data types to perform conversion.
Examples include str(), int(), float(), and bool().
"""
a = str(25)         # "25"
b = float("3.14")   # 3.14
c = int(3.99)       # 3 (decimal part truncated)
d = bool("")        # False (empty string is False)
e = bool("hi")      # True (non-empty string is True)

print(a, b, c, d, e)  # Output: 25 3.14 3 False True

# ---------------------------------------------
# ⚠️ Note:
"""
Invalid conversions will raise errors:
Examples:
int("hello")   # ❌ ValueError
float("abc")   # ❌ ValueError
Always validate inputs when casting user-provided data.
"""
