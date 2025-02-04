Here are several practice exercises and examples for understanding **bitwise operators** in Python. These exercises cover a range of use cases, from basic operations to more advanced applications like flag management, binary data manipulation, and efficient algorithms. Try solving these to improve your skills!

---

### **1. Basic Bitwise Operations**
Perform bitwise operations on two integers `a` and `b` and print the results for each operation.

#### Example:
```python
a = 60  # 111100 in binary
b = 13  # 001101 in binary

# Perform the following operations:
# AND
print("a & b =", a & b)

# OR
print("a | b =", a | b)

# XOR
print("a ^ b =", a ^ b)

# NOT (inverts the bits)
print("~a =", ~a)

# Left shift
print("a << 2 =", a << 2)

# Right shift
print("a >> 2 =", a >> 2)
```

#### Expected Output:
```
a & b = 12    (1100 in binary)
a | b = 61    (111101 in binary)
a ^ b = 49    (110001 in binary)
~a = -61      (invert all bits of a)
a << 2 = 240  (shift left, multiply by 2^2)
a >> 2 = 15   (shift right, divide by 2^2)
```

---

### **2. Check if a Number is Even or Odd Using Bitwise Operators**
Use the **bitwise AND** operator to check if a number is even or odd.

#### Example:
```python
def is_even_or_odd(num):
    if num & 1:
        return "Odd"
    else:
        return "Even"

# Test the function with different numbers
print(is_even_or_odd(7))  # Odd
print(is_even_or_odd(10))  # Even
print(is_even_or_odd(3))  # Odd
```

---

### **3. Set, Clear, and Toggle Flags Using Bitwise Operators**
Use bitwise operations to simulate setting, clearing, and toggling flags in an integer. Assume we have an integer that stores multiple flags in different bits.

#### Example:
```python
# Initial flag state (0000)
flags = 0

# Set the 2nd flag (binary: 0010)
flags |= 0b0010
print(f"Flags after setting 2nd flag: {bin(flags)}")

# Clear the 2nd flag (binary: 0000)
flags &= ~0b0010
print(f"Flags after clearing 2nd flag: {bin(flags)}")

# Toggle the 1st flag (binary: 0001)
flags ^= 0b0001
print(f"Flags after toggling 1st flag: {bin(flags)}")
```

#### Expected Output:
```
Flags after setting 2nd flag: 0b10
Flags after clearing 2nd flag: 0b0
Flags after toggling 1st flag: 0b1
```

---

### **4. XOR to Find the Missing Number in a Sequence**
Given an array of integers, one number is missing in the sequence from 1 to `n`. Use XOR to find the missing number.

#### Example:
```python
def find_missing_number(arr, n):
    total_xor = 0
    for i in range(1, n + 1):
        total_xor ^= i  # XOR all numbers from 1 to n
    
    for num in arr:
        total_xor ^= num  # XOR all elements in the array
    
    return total_xor

# Example usage
arr = [1, 2, 4, 5, 6]
n = 6  # Expected sequence from 1 to 6
missing_number = find_missing_number(arr, n)
print(f"Missing number: {missing_number}")
```

#### Expected Output:
```
Missing number: 3
```

---

### **5. Convert a Decimal Number to Binary Using Bitwise Operations**
Write a function that converts a decimal number to its binary representation using bitwise operations.

#### Example:
```python
def decimal_to_binary(n):
    binary_rep = ""
    while n > 0:
        binary_rep = str(n & 1) + binary_rep  # Add the LSB to the front
        n >>= 1  # Right shift to process the next bit
    return binary_rep if binary_rep else "0"

# Test the function
print(decimal_to_binary(10))  # Output: 1010
print(decimal_to_binary(255))  # Output: 11111111
```

#### Expected Output:
```
1010
11111111
```

---

### **6. Count the Number of Set Bits (1s) in a Number**
Count how many bits are set to 1 (also known as Hamming weight or population count) in the binary representation of a number.

#### Example:
```python
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1  # Increment count if the LSB is 1
        n >>= 1  # Right shift to check the next bit
    return count

# Test the function
print(count_set_bits(10))  # Output: 2 (binary 1010)
print(count_set_bits(255))  # Output: 8 (binary 11111111)
```

#### Expected Output:
```
2
8
```

---

### **7. Swap Two Numbers Using Bitwise XOR**
Swap two numbers without using a temporary variable. This is a common trick using XOR.

#### Example:
```python
def swap(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    a ^= b
    b ^= a
    a ^= b
    print(f"After swap: a = {a}, b = {b}")

# Test the swap function
swap(5, 10)
```

#### Expected Output:
```
Before swap: a = 5, b = 10
After swap: a = 10, b = 5
```

---

### **8. Implement a Simple Encryption Using XOR**
Implement a simple encryption and decryption function using XOR.

#### Example:
```python
def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(char) ^ key) for char in data)

# Example usage
data = "hello"
key = 123

# Encrypt the message
encrypted = xor_encrypt_decrypt(data, key)
print(f"Encrypted: {encrypted}")

# Decrypt the message
decrypted = xor_encrypt_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
```

#### Expected Output:
```
Encrypted:  (Encrypted gibberish)
Decrypted: hello
```

---

### **9. Use Bitwise Operators to Determine if a Number is a Power of Two**
A number is a power of two if it has exactly one bit set to `1` in its binary representation. You can use bitwise operations to check this.

#### Example:
```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Test the function
print(is_power_of_two(16))  # Output: True (2^4)
print(is_power_of_two(18))  # Output: False
```

#### Expected Output:
```
True
False
```

---

### **10. Using Bitwise Operators for Range of Values**
Consider an integer where each bit represents a different option. Write a program that uses bitwise operations to determine if a number is within a specific range.

#### Example:
```python
def is_in_range(value, min_val, max_val):
    return min_val <= value <= max_val

# Test the function
print(is_in_range(5, 1, 10))  # True
print(is_in_range(15, 1, 10))  # False
```

---

### **Additional Challenges**

1. **Find the First Set Bit**: Given an integer, find the position of the first set bit (bit with value `1`).
   
2. **Binary Inversion**: Write a function to invert all bits of a number up to a certain bit-width.

3. **Reverse the Bits of a Number**: Write a function that reverses the bits of a number.

4. **Check if Two Numbers Have Opposite Signs**: Use bitwise operators to check if two numbers have opposite signs.

---

### **Conclusion**
These exercises are a great way to practice and understand bitwise operators. By completing them, you'll become proficient in using bitwise operators for a variety of tasks, from simple operations like checking if a number is odd/even to more advanced tasks like encryption, binary manipulations, and more!