### **Differences Between Functions, Modules, and Packages in Python**  

| Feature | **Function** | **Module** | **Package** |
|---------|------------|-----------|------------|
| **Definition** | A block of reusable code that performs a specific task | A file containing Python code (functions, classes, variables) | A directory containing multiple modules with an `__init__.py` file |
| **Purpose** | Encapsulates logic for reuse | Organizes related functions & classes | Organizes multiple modules into a structured hierarchy |
| **File Format** | Defined inside a `.py` file | A `.py` file (e.g., `math.py`) | A folder containing an `__init__.py` file and modules |
| **Scope** | Limited to where it is defined or imported | Can be imported using `import module_name` | Can contain sub-packages and modules |
| **Example** | `def add(a, b): return a + b` | `math.py` containing `def add(a, b): return a + b` | `mypackage/` with `module1.py` and `module2.py` |
| **Usage** | Called directly in code | Imported with `import module_name` | Imported with `import package.module_name` |
| **Example Import** | Not needed (already defined in the script) | `import math` | `from mypackage import module1` |

---

### **Example of Function**
```python
def greet(name):
    return f"Hello, {name}!"
```
Usage:
```python
print(greet("Alice"))  # Output: Hello, Alice!
```

---

### **Example of Module**
#### **math_utils.py (Module)**
```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```
Usage in another script:
```python
import math_utils

print(math_utils.add(2, 3))  # Output: 5
print(math_utils.multiply(2, 3))  # Output: 6
```

---

### **Example of Package**
#### **mypackage (Package)**
```
mypackage/
│── __init__.py  # Marks it as a package
│── module1.py
│── module2.py
```
#### **mypackage/module1.py**
```python
def hello():
    return "Hello from Module 1!"
```
#### **mypackage/module2.py**
```python
def world():
    return "World from Module 2!"
```
Usage:
```python
from mypackage import module1, module2

print(module1.hello())  # Output: Hello from Module 1!
print(module2.world())  # Output: World from Module 2!
```

---

### **Key Takeaways**
- **Functions**: Small, reusable code blocks.
- **Modules**: Python files containing functions and classes.
- **Packages**: Folders containing multiple related modules.

Let me know if you need a deeper explanation! 🚀