## **🔹 Introduction to Data Types in Python**  
Python is a dynamically typed language, meaning you don't need to declare variable types explicitly—they are inferred automatically.  

### **🔸 Primary Data Types in Python**
| Data Type  | Description | Example |
|------------|------------|---------|
| `int` | Integer numbers | `x = 10` |
| `float` | Decimal numbers | `y = 3.14` |
| `str` | Text (sequence of characters) | `name = "Alice"` |
| `bool` | Boolean values (`True` or `False`) | `is_active = True` |
| `NoneType` | Represents "nothing" | `value = None` |

---

## **🔹 Numeric Data Types**
Python supports **integers, floats, and complex numbers**.

```python
a = 10       # Integer
b = 3.14     # Float
c = 2 + 3j   # Complex number

print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'complex'>
```

### **🔸 Arithmetic Operations**
```python
x = 10
y = 3

print(x + y)  # Addition -> 13
print(x - y)  # Subtraction -> 7
print(x * y)  # Multiplication -> 30
print(x / y)  # Division -> 3.3333
print(x // y) # Floor Division -> 3
print(x % y)  # Modulus -> 1
print(x ** y) # Exponentiation -> 10^3 = 1000
```

---

## **🔹 String Data Type**
A **string** is a sequence of characters enclosed in **single (`'`) or double (`"`) quotes**.

```python
s1 = "Hello"
s2 = 'World'

print(s1 + " " + s2)  # Output: Hello World
print(len(s1))  # Output: 5 (length of string)
```

### **🔸 String Indexing & Slicing**
```python
text = "Python"

print(text[0])   # 'P' (First character)
print(text[-1])  # 'n' (Last character)
print(text[1:4]) # 'yth' (Substring from index 1 to 3)
```

### **🔸 Common String Methods**
```python
message = "  Hello, Python!  "

print(message.lower())   # '  hello, python!  '
print(message.upper())   # '  HELLO, PYTHON!  '
print(message.strip())   # 'Hello, Python!' (Removes spaces)
print(message.replace("Python", "World"))  # '  Hello, World!  '
print(message.split(","))  # ['  Hello', ' Python!  ']
```

---

## **🔹 Boolean Data Type**
Booleans represent **True** or **False** values.

```python
is_valid = True
is_empty = False

print(type(is_valid))  # Output: <class 'bool'>

# Boolean operations
print(5 > 3)  # True
print(5 == 3) # False
print(5 != 3) # True
```

---

## **🔹 NoneType (Null Value)**
The `None` keyword represents the absence of a value.

```python
data = None
print(data)        # Output: None
print(type(data))  # Output: <class 'NoneType'>
```

---

## **🔹 Type Conversion (Casting)**
You can convert between different data types using `int()`, `float()`, `str()`, and `bool()`.

```python
x = "100"

y = int(x)   # Convert string to integer
z = float(x) # Convert string to float

print(y + 5)  # Output: 105
print(z + 2.5) # Output: 102.5
```
