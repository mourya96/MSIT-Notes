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