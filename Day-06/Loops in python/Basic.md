Loops in Python are used to execute a block of code repeatedly as long as a condition is met or for a specific number of iterations. Python provides two types of loops:

1. **For Loop**
2. **While Loop**

### 1. **For Loop**
The `for` loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary, string, or range). It executes a block of code for each element in the sequence.

#### Syntax:
```python
for item in sequence:
    # Code block to execute
```

#### Example:
```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

#### Output:
```
apple
banana
cherry
```

#### Example with `range()`
The `range()` function generates a sequence of numbers. It is often used with `for` loops for a specific number of iterations.

```python
for i in range(5):  # Iterates from 0 to 4
    print(i)
```

#### Output:
```
0
1
2
3
4
```

You can also specify a **start**, **stop**, and **step** value in `range()`.

```python
for i in range(2, 10, 2):  # Start at 2, stop at 10, step by 2
    print(i)
```

#### Output:
```
2
4
6
8
```

---

### 2. **While Loop**
A `while` loop repeatedly executes a block of code as long as the condition specified is `True`. The condition is evaluated before each iteration.

#### Syntax:
```python
while condition:
    # Code block to execute
```

#### Example:
```python
# Simple example: Print numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment count to avoid an infinite loop
```

#### Output:
```
1
2
3
4
5
```

### **Breaking and Continuing in Loops**

#### 1. `break`
The `break` statement is used to exit the loop prematurely, regardless of the condition.

#### Example:
```python
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
```

#### Output:
```
0
1
2
3
4
```

#### 2. `continue`
The `continue` statement is used to skip the current iteration and continue to the next one, bypassing the rest of the code inside the loop for that iteration.

#### Example:
```python
for i in range(10):
    if i == 5:
        continue  # Skip the rest of the loop when i is 5
    print(i)
```

#### Output:
```
0
1
2
3
4
6
7
8
9
```

### **Nested Loops**
You can also have loops inside other loops, which are called **nested loops**. They are commonly used to iterate over multi-dimensional data structures (like a list of lists).

#### Example:
```python
# Nested for loop
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")
```

#### Output:
```
i = 0, j = 0
i = 0, j = 1
i = 1, j = 0
i = 1, j = 1
i = 2, j = 0
i = 2, j = 1
```

---

### **Looping Through Dictionaries**
When iterating over a dictionary, you can loop through the keys, values, or both.

#### Example: Looping through keys
```python
my_dict = {"a": 1, "b": 2, "c": 3}
for key in my_dict:
    print(key)  # Prints the keys
```

#### Output:
```
a
b
c
```

#### Example: Looping through values
```python
for value in my_dict.values():
    print(value)  # Prints the values
```

#### Output:
```
1
2
3
```

#### Example: Looping through both keys and values
```python
for key, value in my_dict.items():
    print(f"{key}: {value}")  # Prints both key and value
```

#### Output:
```
a: 1
b: 2
c: 3
```

---

### **Infinite Loops**
A loop that never terminates is known as an **infinite loop**. It happens when the condition is always `True`. You can use a `break` statement to exit the infinite loop.

#### Example of Infinite Loop:
```python
while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input == 'exit':
        break
    else:
        print("You entered:", user_input)
```

This loop will keep asking for input until the user types "exit".

---

### **Loop with `else`**
A loop in Python can have an `else` block, which will be executed when the loop completes normally (without encountering a `break` statement). The `else` block is not executed if the loop is terminated via `break`.

#### Example:
```python
for i in range(5):
    print(i)
else:
    print("Loop finished without break.")
```

#### Output:
```
0
1
2
3
4
Loop finished without break.
```

If you use `break` inside the loop, the `else` block won't execute.

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop finished without break.")
```

#### Output:
```
0
1
2
```

The "Loop finished without break." message is **not printed** because the loop was terminated using `break`.

---

### **Conclusion**
Loops in Python are a powerful and essential feature, allowing you to repeat tasks efficiently. Here's a quick summary:

- **For Loop**: Useful for iterating over sequences (like lists, strings, or ranges).
- **While Loop**: Repeats code while a condition is true.
- **Break**: Exits the loop early.
- **Continue**: Skips to the next iteration of the loop.
- **Nested Loops**: Allows loops within loops.
- **Looping through dictionaries**: Iterate over keys, values, or both.
- **`else` with loops**: Executes after a loop completes, unless the loop is interrupted by `break`.

Mastering loops will help you tackle repetitive tasks in Python and implement efficient algorithms for a wide range of problems!