Python provides several built-in data structures, each serving different purposes. These data structures allow you to store and organize data in various ways. Here's a quick overview of the most commonly used built-in data structures in Python:

### 1. **Lists**
Lists are ordered collections of items that are mutable (i.e., their contents can be changed). They are one of the most commonly used data structures in Python.

#### Key Features:
- Ordered: The order of elements is preserved.
- Mutable: You can change elements, append new ones, and remove existing ones.
- Can hold elements of different types.

#### Example:

```python
# Create a list
fruits = ["apple", "banana", "cherry"]

# Access elements
print(fruits[0])  # Output: apple

# Modify elements
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']

# Add elements
fruits.append("mango")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'mango']

# Remove elements
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'orange', 'mango']
```

---

### 2. **Tuples**
Tuples are similar to lists but are **immutable**, meaning once created, their contents cannot be changed. Tuples are often used to store collections of data that shouldn't be modified.

#### Key Features:
- Ordered: The order of elements is preserved.
- Immutable: You cannot modify, add, or remove elements.
- Can hold elements of different types.

#### Example:

```python
# Create a tuple
point = (10, 20)

# Access elements
print(point[0])  # Output: 10

# Tuples are immutable, so you can't change their values
# point[0] = 30  # This will raise a TypeError

# Nested tuple
nested_tuple = (1, 2, (3, 4))
print(nested_tuple[2][0])  # Output: 3
```

---

### 3. **Dictionaries (dict)**
Dictionaries are unordered collections of key-value pairs. Each key is unique, and values can be of any data type. Dictionaries are mutable and commonly used when you need to associate one piece of data (a key) with another (a value).

#### Key Features:
- Unordered (Python 3.7+ maintains insertion order).
- Mutable: You can add, modify, and remove key-value pairs.
- Keys must be unique and immutable (e.g., strings, numbers, tuples).

#### Example:

```python
# Create a dictionary
person = {"name": "John", "age": 30, "city": "New York"}

# Access values
print(person["name"])  # Output: John

# Modify values
person["age"] = 31
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Add new key-value pair
person["job"] = "Engineer"
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

# Remove a key-value pair
del person["city"]
print(person)  # Output: {'name': 'John', 'age': 31, 'job': 'Engineer'}
```

---

### 4. **Sets**
Sets are unordered collections of unique elements. They are often used when you need to store a collection of items without duplicates and perform set operations like unions, intersections, and differences.

#### Key Features:
- Unordered: The order of elements is not preserved.
- Mutable: You can add and remove elements.
- Only unique elements are stored.

#### Example:

```python
# Create a set
fruits_set = {"apple", "banana", "cherry"}

# Add elements
fruits_set.add("mango")
print(fruits_set)  # Output: {'banana', 'mango', 'cherry', 'apple'}

# Remove elements
fruits_set.remove("banana")
print(fruits_set)  # Output: {'mango', 'cherry', 'apple'}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 & set2)  # Intersection: {3}
print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
print(set1 - set2)  # Difference: {1, 2}
```

---

### 5. **Strings**
Although strings are not typically considered a "data structure" in Python, they are a built-in type that functions as a sequence of characters. Strings in Python are immutable and can be used in many scenarios, such as storing text data or manipulating text.

#### Key Features:
- Immutable: You cannot modify individual characters in a string.
- Ordered: Characters maintain their order.
- Supports various operations like slicing, concatenation, and formatting.

#### Example:

```python
# Create a string
text = "Hello, World!"

# Access characters
print(text[0])  # Output: H

# String slicing
print(text[7:12])  # Output: World

# String concatenation
new_text = text + " How are you?"
print(new_text)  # Output: Hello, World! How are you?

# String formatting
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)  # Output: Hello, Alice!
```

---

### 6. **Byte Sequences**
Python also provides built-in types for working with binary data:
- **bytes**: Immutable sequences of bytes.
- **bytearray**: Mutable sequences of bytes.

These are often used in tasks such as handling binary data from files, network protocols, or working with encoded data.

#### Example (bytes):
```python
# Create a bytes object
data = b"Hello, World!"
print(data)  # Output: b'Hello, World!'
```

#### Example (bytearray):
```python
# Create a bytearray object
data = bytearray([65, 66, 67])
print(data)  # Output: bytearray(b'ABC')

# Modify the bytearray
data[0] = 90
print(data)  # Output: bytearray(b'ZBC')
```

---

### 7. **Arrays (from the `array` module)**
The `array` module provides a more efficient way to store elements of the same type than lists. This is useful when you need to store large amounts of numerical data and want to optimize for performance and memory usage.

#### Key Features:
- Allows you to store data more efficiently than lists, but all elements must be of the same type.
- Offers more control over how data is stored and accessed.

#### Example:

```python
import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Access and modify elements
print(arr[0])  # Output: 1
arr[0] = 10
print(arr)  # Output: array('i', [10, 2, 3, 4, 5])
```

---

### Summary of Python's Built-in Data Structures

- **Lists**: Ordered, mutable collections of elements.
- **Tuples**: Ordered, immutable collections of elements.
- **Dictionaries (dict)**: Unordered collections of key-value pairs, mutable.
- **Sets**: Unordered collections of unique elements.
- **Strings**: Ordered, immutable sequences of characters (often used for text).
- **Byte Sequences**: `bytes` (immutable) and `bytearray` (mutable) for binary data.
- **Arrays**: More efficient than lists for storing large numbers of elements of the same type (using the `array` module).

These data structures are the building blocks for managing and processing data in Python. Depending on the use case, you can select the most appropriate one to optimize performance, memory usage, and ease of manipulation.