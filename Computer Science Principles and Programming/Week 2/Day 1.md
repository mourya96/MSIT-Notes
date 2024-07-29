# Day 1

## Data Types

The different data types used in python are:

- Numbers
  - Integers (int)
  - Rational numbers (float)
- Text
  - String -> Represented in double quotes "" and single quotes ''
  - Example: "Hello", 'Hi'
- Truth Values
  - True or False (bool) -> boolean
  - Example: 8 < 5 -> False

The mathematical operations we can perform on **numbers** are:

- Addition - Represented with **+** sign
- Subtraction - Represented with **-** sign
- Multiplication - Represented with **\*** sign
- Division - Represented with **\/** sign
- Power/Exponent - Represented with **\*\*** sign

Normally if we perform a mathematical operation with an **integer** with a **float** the integer number initially gets converted into **float** and the operation is done.

The mathematical operations with a **string** are:

- Addition - "abc" + "def" = "abcdef"
- Multiplication - "Abc"*3 = "AbcAbcAbc"
  - **Note**: We cannot multiply strings with float numbers.

Any other operations with strings will result in errors.

However we can perform comparatative operations with numbers and strings such as:

- == -> Equal to
- != -> Inequal to
- \>= -> Greater than and equal to
- <= -> Lesser than and equal to
- \> -> Greater than
- < -> Lesser than

The comparision operation always results in boolean value (True or False).

## Variables

To reuse a value (number/string/bool), we need to store it in a memory. To do this, we assign these values to a variable.

Example: a = 2

- Here a is called variable name
- 2 is the value
- = sign is called assignment operator
- So here, we are assigning 2 to the variable called a which results it in storing it in a memory.

Example:

```py
a = 4
b = 7
b = a - 2
a = a + 1
```

Here we are assigning 4 and 7 to a and b respectively. In the third statement we are assigning b again to the result of `a - 2`. So python performs the operation `a-2` first which is 2 and this result is stored in `b`. So the previous value in b which 7 gets overwritten by the value 2. Hence the new value of b is 2.

Again same thing happens with the `a`. The result of `a + 1` overwrites the previous value of `a`.
