# Task 1
int_val = 1
print("Initial integer variable:", int_val)
int_val = 2 # Changed the int value to 2
print("Changed integer value:",int_val)

float_val = 1.1
print("Initial float value:", float_val)
float_val = 2.2 # Changed the float value to 2.2
print("Changed float value:", float_val)

string_val = "MS"
print("Initial string value:", string_val)
string_val = "MSIT" # Changed the string value to MSIT
print("Changed string value:", string_val)

a = 100
b = 0
print("Before swap:", "a =", a ,"b =" ,b)
a, b = b, a # Swapping the numbers
print("After swap:", "a =" , a, "b =" ,b)

# Task 2

int_val = 1
float_val = 1.1
string_val = 'MSIT'
bool_val = True

print("Integer: Type", type(int_val), "Value =", int_val)
print("Float: Type", type(float_val), "Value =", float_val)
print("String: Type", type(string_val), "Value =", string_val)
print("Boolean: Type", type(bool_val), "Value =", bool_val)

print("Integer to Float:", float(int_val))
print("Float to Integer:", int(float_val))
print("Float to String:", str(float_val))

# Task 3

# Declaring an integer variable
int_val = 1 
# Here the int_val stores the value 1 in the memory. Because 1 is an integer, the data type of int_val is integer


# Declaring a float variable
float_val = 1.1 
# Here the float_val stores the value 1.1 in the memory. Because 1.1 is a rational number, the data type of float_val is float


# Declaring a string variable
string_val = 'MSIT'
# Here the string_val stores the value 'MSIT' in the memory. 

# Declaring a boolean variable
bool_val = True 
# The value True is stored in memory with the variable name bool_val.

# Name Error
print(Int_val)
# NameError: name 'Int_val' is not defined. Did you mean: 'int_val'?
# The above comment contains the error message. We know that variable names in python are case sensitive both 'Int_val' and 'int_val' are different
# Since we didn't define Int_val, it gives us the name error.


# Task 4

Syntax Error

a = 'Hello'
"Syntax Error" = a
# SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

a = 5
print(A)
# NameError: name 'A' is not defined. Did you mean: 'a'?

a = "Hello"
print(int(a))
# ValueError: invalid literal for int() with base 10: 'Hello'

a = "Hello"
print(a*3.5)
# TypeError: can't multiply sequence by non-int of type 'float'

a = 5
print(a/0)
# ZeroDivisionError: division by zero

import numpy as np
print(np.arange(10))
# ModuleNotFoundError: No module named 'numpy'