## **🚀 Advanced String Manipulation & Formatting in Python**

Python provides powerful tools for string manipulation and formatting. Let's dive deep into some advanced techniques that will help you write cleaner and more efficient code!  

---

## **🔹 1. String Manipulation Techniques**

### **🔸 a) String Slicing**
```python
text = "Python Programming"

print(text[0:6])   # 'Python' (Substring from index 0 to 5)
print(text[-3:])   # 'ing' (Last 3 characters)
print(text[::-1])  # 'gnimmargorP nohtyP' (Reversed string)
```

### **🔸 b) String Methods**
```python
s = "  Hello, Python!  "

print(s.strip())    # Removes leading/trailing spaces -> 'Hello, Python!'
print(s.lower())    # Converts to lowercase -> '  hello, python!  '
print(s.upper())    # Converts to uppercase -> '  HELLO, PYTHON!  '
print(s.title())    # Capitalizes first letter of each word -> '  Hello, Python!  '
print(s.swapcase()) # Swaps case -> '  hELLO, pYTHON!  '
print(s.replace("Python", "World"))  # '  Hello, World!  '
```

### **🔸 c) Checking and Finding Substrings**
```python
s = "hello world"

print(s.startswith("hello"))  # True
print(s.endswith("world"))    # True
print(s.find("o"))            # First occurrence index (4)
print(s.count("o"))           # Count occurrences (2)
```

---

## **🔹 2. Advanced String Formatting Techniques**

### **🔸 a) Using `format()` Method**
```python
name = "Alice"
age = 25

print("My name is {} and I am {} years old.".format(name, age))
print("My name is {1} and I am {0} years old.".format(age, name))  # Positional arguments
print("My name is {n} and I am {a} years old.".format(n=name, a=age))  # Named placeholders
```

### **🔸 b) f-Strings (Python 3.6+) – Faster and Cleaner**
```python
name = "Bob"
age = 30

print(f"My name is {name} and I am {age} years old.")
print(f"Next year, I will be {age + 1} years old.")
```

✅ **F-strings can also format numbers:**
```python
pi = 3.1415926535
print(f"Pi rounded to 2 decimal places: {pi:.2f}")  # 3.14
print(f"Pi rounded to 5 decimal places: {pi:.5f}")  # 3.14159
```

✅ **Using f-strings for debugging (Python 3.8+):**
```python
x = 10
y = 20
print(f"{x=} and {y=}")  # x=10 and y=20
```

---

## **🔹 3. Handling Multiline Strings**
```python
multiline = """This is a
multi-line string
in Python."""
print(multiline)
```

✅ **Using `\n` for new lines:**
```python
multiline = "This is line 1.\nThis is line 2."
print(multiline)
```

---

## **🔹 4. Joining and Splitting Strings**
### **🔸 a) Splitting a String**
```python
s = "apple,banana,grape"

fruits = s.split(",")  # ['apple', 'banana', 'grape']
print(fruits)
```

### **🔸 b) Joining a List of Strings**
```python
words = ["Python", "is", "awesome"]
sentence = " ".join(words)  # "Python is awesome"
print(sentence)
```

---

## **🔹 5. Removing Unwanted Characters**
```python
s = "@Hello#"
print(s.strip("@#"))  # 'Hello'
```

---

## **🔹 6. Encoding and Decoding Strings**
```python
s = "Hello"
encoded = s.encode("utf-8")
decoded = encoded.decode("utf-8")

print(encoded)  # b'Hello' (Bytes)
print(decoded)  # 'Hello' (String)
```

---

## **🔹 7. Regular Expressions (Regex) for String Manipulation**
Python’s `re` module provides powerful tools for pattern matching.

```python
import re

text = "My email is example@gmail.com"

match = re.search(r'\S+@\S+', text)  # Find email in text
print(match.group())  # 'example@gmail.com'
```

---

### **💡 What's Next?**
Do you want to explore **Regex in-depth, working with JSON/XML, or performance optimization tips for string handling?** Let me know! 🚀