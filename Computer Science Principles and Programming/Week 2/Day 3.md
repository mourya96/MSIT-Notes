# Day 3

## Functions

Functions are programming constructs that allow us to repeat a task multiple times with different inputs at any time. Generally a function contains:

- Name of the function
- Inputs (arguments of the function)
- Body of the function
- Output - Return value of the function. If a function does not return any value then there is no output to that function.

There are two types of function:

- In built: Functions that are already defined. Example: `print`, `input`, `abs` etc.
- User defined: Functions that are defined by the user. To define these functions we use a keyword called `def`.

```python
def add(a:int, b:int) -> int:
    return a + b
```

Here, using the keyword `def` we defined a "user-defined" function called `add` which is the function name. The inputs are a and b which are integers. Then it returns the sum of those numbers.

## Function `input()`

The function `input()` takes the control of the terminal and waits for the input of the user. The output of `input()` function is always a string (`str`).

So we convert the output of `input()` to the respective data types using type casting.

For example we use `int(input())` to take the input from the terminal and convert the output of the `input()` function to integers using `int` function.

We can call functions inside the function. However the innner most function gets executed first, then the second inner most and so on...

Finally, the outer most function gets executed at last.
