### **Variable Scope and Lifetime in Python**

In Python, the **scope** of a variable refers to the part of the program where the variable is accessible. The **lifetime** of a variable refers to how long the variable exists in memory during the execution of the program.

### **1. Types of Variable Scope in Python**

Python has several types of variable scopes, which determine where variables can be accessed and modified:

#### **1.1. Local Scope**
A variable is in **local scope** when it is declared inside a function or block. The variable can only be accessed or modified within that specific function.

- **Example**:
```python
def my_function():
    local_variable = 10  # Local variable
    print(local_variable)

my_function()
# print(local_variable)  # This will raise an error because local_variable is not accessible outside the function.
```

In this case, `local_variable` is only accessible within `my_function` and cannot be accessed from outside it.

#### **1.2. Enclosing Scope (Nonlocal Scope)**
If a variable is declared in a function that is enclosing another function (i.e., a **nested function**), that variable is in the **enclosing scope**.

- **Example**:
```python
def outer_function():
    enclosing_variable = 20  # Enclosing variable

    def inner_function():
        print(enclosing_variable)  # Accessing enclosing_variable from outer_function
    inner_function()

outer_function()  # Output: 20
```

Here, `enclosing_variable` is declared in the `outer_function` and is accessible to `inner_function`, which is in the nested scope. It is in the **enclosing scope**.

#### **1.3. Global Scope**
A variable is in **global scope** if it is declared outside of all functions or blocks. Global variables are accessible from anywhere in the code, including within functions, unless a local variable with the same name is defined.

- **Example**:
```python
global_variable = 30  # Global variable

def my_function():
    print(global_variable)  # Accessing global variable inside a function

my_function()  # Output: 30
print(global_variable)  # Output: 30
```

Here, `global_variable` is accessible both inside the function and outside because it is in the global scope.

#### **1.4. Built-in Scope**
The **built-in scope** refers to the scope that contains Python’s built-in objects and functions (e.g., `print()`, `len()`, `max()`, etc.). These are available globally across all Python programs.

- **Example**:
```python
print("Hello, World!")  # 'print' is a built-in function
```

Built-in functions and exceptions, like `print()`, `range()`, and `Exception`, are part of the built-in scope.

---

### **2. Variable Lifetime**

The **lifetime** of a variable refers to the period during which the variable exists in memory.

- **Local variables** exist only as long as the function or block in which they are defined is executing.
- **Global variables** exist throughout the lifetime of the program, from the time they are declared until the program terminates.

#### **2.1. Lifetime of Local Variables**
- A local variable’s lifetime begins when the function in which it is declared is called and ends when the function terminates (i.e., when the function’s execution is complete). 
- Once the function execution ends, the local variable is destroyed, and it no longer exists in memory.

#### **2.2. Lifetime of Global Variables**
- A global variable’s lifetime starts when the program begins and continues until the program ends.
- Global variables are accessible throughout the program’s execution, even if they are passed between different functions.

#### **2.3. Lifetime of Built-in Variables**
- Built-in variables exist throughout the execution of the program and are always available for use.

---

### **3. Scope Resolution (LEGB Rule)**

Python follows the **LEGB rule** to resolve variable names:
1. **Local**: The innermost scope, i.e., the current function.
2. **Enclosing**: The scope of any enclosing functions, starting with the outermost function.
3. **Global**: The global scope of the module.
4. **Built-in**: The built-in Python functions and objects.

Python will search for a variable in the **LEGB** order and return the first matching variable it finds.

#### **Example**:
```python
x = "Global"

def outer_function():
    x = "Enclosing"

    def inner_function():
        x = "Local"
        print(x)  # Python will use the 'x' from the local scope of inner_function

    inner_function()

outer_function()  # Output: Local
```

- **Inside `inner_function`**, Python uses the **local variable** `x`.
- **If `x` were not defined in the local scope**, Python would move to the **enclosing scope** (from `outer_function`).
- If `x` were not found in the enclosing scope, it would move to the **global scope**.

---

### **4. Global vs Local Variables**

If a variable with the same name exists both in the **global scope** and within a function, the **local variable** will take precedence within that function unless explicitly stated with the `global` keyword.

#### **Example with Global Variable**:
```python
x = 100  # Global variable

def my_function():
    global x  # Declare that we want to use the global x
    x = 200  # Modify the global variable
    print(x)

my_function()  # Output: 200
print(x)  # Output: 200 (the global x was modified)
```

#### **Example without `global`**:
```python
x = 100  # Global variable

def my_function():
    x = 200  # This creates a new local variable, not modifying the global one
    print(x)

my_function()  # Output: 200
print(x)  # Output: 100 (global variable remains unchanged)
```

---

### **5. The `nonlocal` Keyword**
In the case of **nested functions**, you can use the `nonlocal` keyword to modify a variable in the **enclosing scope**, rather than creating a new local variable.

#### **Example**:
```python
def outer_function():
    x = 10  # Enclosing variable

    def inner_function():
        nonlocal x  # Modify the enclosing variable
        x = 20  # Now we modify the enclosing x, not create a new local x
        print(x)

    inner_function()  # Output: 20
    print(x)  # Output: 20 (the enclosing variable is modified)

outer_function()
```

---

### **6. Key Points to Remember**
- **Local scope**: Variables inside functions, accessible only within the function.
- **Enclosing scope**: Variables in outer functions, accessible in inner functions.
- **Global scope**: Variables declared outside functions, accessible throughout the program.
- **Built-in scope**: Variables and functions provided by Python, accessible everywhere.
- The **LEGB rule** determines the order in which Python searches for variable names.
- The **lifetime** of local variables is tied to the function’s execution, while global variables exist for the duration of the program.
- Use `global` and `nonlocal` to modify variables in global and enclosing scopes from within functions.

---

Let me know if you need any further clarifications or examples!