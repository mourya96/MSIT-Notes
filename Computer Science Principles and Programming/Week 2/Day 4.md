# Day 4

## Functions

Generally there are two types of functions:

- Built-in (or) libraries
- User Defined Functions

To use the built-in functions, we import libraries using the keyword `import`.

Example: `import math`

In the above statement we are importing the `math` libary using `import` keyword. We can use functions in the math library such as `log(), radians(), ceil(), floor()`, etc.

Example:

```python
import math

print(math.log(64, 2))
```

The statement `math.log(a, b)` is same as $\log_a^b$.

Another libary is `random` library. The functions in `random` library generates a random number.

```python
import random

value_die = random.randint(1,6)
```

The function `randint(a, b)` generates a random integer which is in the range [a, b] (both a and b are included).

```python

import random

random_number = random.random()
```

The function `random()` generates a random number and does not take any inputs in the function.

## User defined functions

Using the keyword `def` we can define the function by ourselves.

Example:

```python

def add(a: int, b: int) -> int:
    return a + b
```

Here the **function name** is `add`, `a` and `b` are called parameters or inputs of the function. The values that are passed to the function are called arguments.
