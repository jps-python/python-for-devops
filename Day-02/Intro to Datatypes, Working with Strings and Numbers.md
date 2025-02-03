
Let's break it down step by step! 🚀  

## **🔹 Introduction to Datatypes in Python**  
In Python, data types define the kind of data a variable can hold. Here are the main built-in types:  

### **🔸 Basic Data Types**
| Data Type  | Description | Example |
|------------|------------|---------|
| `int` | Integer values (whole numbers) | `x = 10` |
| `float` | Decimal/real numbers | `y = 3.14` |
| `str` | Text (string) | `name = "Alice"` |
| `bool` | Boolean values | `is_active = True` |

---

## **🔹 Working with Numbers in Python**
Python supports **integers**, **floats**, and **complex numbers**.

### **🔸 Basic Arithmetic Operations**
```python
a = 10
b = 3

print(a + b)  # Addition (13)
print(a - b)  # Subtraction (7)
print(a * b)  # Multiplication (30)
print(a / b)  # Division (3.3333)
print(a // b) # Floor Division (3)
print(a % b)  # Modulus (1)
print(a ** b) # Exponentiation (10^3 = 1000)
```

✅ *Python follows the **PEMDAS** rule (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction).*

---

## **🔹 Working with Strings**
Strings are sequences of characters enclosed in **single (`'`) or double (`"`) quotes**.

### **🔸 String Basics**
```python
s1 = "Hello"
s2 = 'World'

print(s1 + " " + s2)  # String concatenation (Hello World)
print(s1 * 3)  # Repeating string (HelloHelloHello)
print(len(s1))  # Length of the string (5)
```

### **🔸 String Indexing & Slicing**
```python
text = "Python"

print(text[0])   # First character ('P')
print(text[-1])  # Last character ('n')
print(text[1:4]) # Slicing ('yth')
```

### **🔸 String Methods**
```python
message = "  Hello, Python!  "

print(message.lower())   # Convert to lowercase
print(message.upper())   # Convert to uppercase
print(message.strip())   # Remove spaces
print(message.replace("Python", "World"))  # Replace words
print(message.split(","))  # Split into list ['Hello', ' Python!']
```

---

## **🔹 Type Conversion (Casting)**
You can convert between different data types using `int()`, `float()`, `str()`, etc.

```python
x = "100"
y = int(x)  # Convert string to integer
z = float(x)  # Convert string to float

print(y + 5)  # 105
print(z + 2.5)  # 102.5
```

---

### **Next Steps?**
Do you want to explore **Lists, Tuples, and Dictionaries** next? Or jump into **Control Flow (if-else, loops)?** Let me know! 🚀