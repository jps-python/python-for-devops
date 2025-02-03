# **🚀 Regular Expressions for Text Processing in Python**

Regular Expressions (Regex) are **extremely powerful** for text processing tasks like validation, searching, parsing, cleaning, and formatting strings. Here, I’ll provide an in-depth guide on how to use **Regex** for various **text processing** tasks in Python. 

---

## **🔹 1. Basic Regex Syntax**

### **📌 Special Characters**
| **Character**  | **Description**                        | **Example**           |
|----------------|----------------------------------------|-----------------------|
| `.`            | Any character except newline (`\n`)     | `"a.b"` -> Matches "acb", "a1b" |
| `^`            | Matches the start of a string           | `^abc` -> Matches "abc" in "abc xyz" |
| `$`            | Matches the end of a string             | `abc$` -> Matches "abc" in "xyz abc" |
| `\d`           | Matches any digit (0-9)                 | `\d{3}` -> Matches "123" in "123 abc" |
| `\D`           | Matches any non-digit                  | `\D{2}` -> Matches "ab" in "ab123" |
| `\w`           | Matches any word character (a-z, A-Z, 0-9, _) | `\w+` -> Matches "hello", "world" |
| `\W`           | Matches any non-word character          | `\W+` -> Matches "!" in "hello!" |
| `\s`           | Matches any whitespace character        | `\s+` -> Matches space between words |
| `\S`           | Matches any non-whitespace character    | `\S+` -> Matches "hello" in "hello world" |
| `[]`           | Matches any one of the characters inside | `[aeiou]` -> Matches any vowel |
| `|`            | OR operator, matches either pattern     | `abc|xyz` -> Matches "abc" or "xyz" |
| `()`           | Groups multiple tokens together        | `(abc|xyz)\d+` -> Matches "abc123" or "xyz456" |

---

## **🔹 2. Text Processing with Regex**

### **📌 a) Matching Specific Patterns**

#### **✔ Match Email**
A simple regex for matching email addresses.
```python
import re
text = "My email is test@example.com"
match = re.search(r'\S+@\S+', text)
if match:
    print("Found email:", match.group())
```
**Output:**
```
Found email: test@example.com
```

#### **✔ Match Phone Number**
Matching phone numbers in the format `xxx-xxx-xxxx`.
```python
phone_number = "123-456-7890"
match = re.match(r'\d{3}-\d{3}-\d{4}', phone_number)
if match:
    print("Valid phone number:", match.group())
```
**Output:**
```
Valid phone number: 123-456-7890
```

---

### **📌 b) Search for Multiple Occurrences**

#### **✔ Extract All Email Addresses**
Using `findall()` to extract all emails from a text:
```python
text = "Here are two emails: user1@example.com, user2@sample.com"
emails = re.findall(r'\S+@\S+', text)
print("Extracted emails:", emails)
```
**Output:**
```
Extracted emails: ['user1@example.com', 'user2@sample.com']
```

#### **✔ Match Multiple Patterns**
```python
text = "The number is 123, and the word is hello"
matches = re.findall(r'\d+|\w+', text)
print(matches)
```
**Output:**
```
['123', 'and', 'the', 'word', 'is', 'hello']
```

---

### **📌 c) Replace Text Using Regex**

#### **✔ Replace Dates (MM-DD-YYYY to YYYY-MM-DD)**
```python
date = "02-15-2023"
new_date = re.sub(r'(\d{2})-(\d{2})-(\d{4})', r'\3-\1-\2', date)
print(new_date)  # Output: "2023-02-15"
```

#### **✔ Remove Non-Alphanumeric Characters**
```python
text = "Hello! How are you? 123."
clean_text = re.sub(r'\W+', ' ', text)  # Replaces non-alphanumeric characters with space
print(clean_text)  # Output: "Hello How are you 123"
```

---

## **🔹 3. Advanced Regex Usage**

### **📌 a) Matching Nested Patterns**

#### **✔ Matching Parentheses (Balanced)**
```python
# Matching text between parentheses
text = "(This is a test)"
match = re.search(r'\(.*\)', text)
if match:
    print("Found:", match.group())
```
**Output:**
```
Found: (This is a test)
```

---

### **📌 b) Word Boundary Matching**
To find a word only if it appears as a whole word (not part of another word).
```python
text = "Python is fun. I love python."
matches = re.findall(r'\bpython\b', text, re.IGNORECASE)
print(matches)  # Output: ['Python', 'python']
```

---

### **📌 c) Lookahead and Lookbehind**

#### **✔ Positive Lookahead**
Match "Python" only if followed by "3":
```python
text = "Python3 is awesome"
match = re.search(r'Python(?=3)', text)
if match:
    print("Matched:", match.group())
```
**Output:**
```
Matched: Python
```

#### **✔ Negative Lookahead**
Match "Python" only if **not** followed by "3":
```python
text = "Python2 is great"
match = re.search(r'Python(?!3)', text)
if match:
    print("Matched:", match.group())
```
**Output:**
```
Matched: Python
```

#### **✔ Positive Lookbehind**
Match "3" only if preceded by "Python":
```python
text = "Python3 is the future"
match = re.search(r'(?<=Python)3', text)
if match:
    print("Matched:", match.group())
```
**Output:**
```
Matched: 3
```

#### **✔ Negative Lookbehind**
Match "3" only if **not** preceded by "Python":
```python
text = "Java3 is popular"
match = re.search(r'(?<!Python)3', text)
if match:
    print("Matched:", match.group())
```
**Output:**
```
Matched: 3
```

---

## **🔹 4. Regex for Text Extraction and Validation**

### **📌 a) Extract Dates (MM-DD-YYYY)**
```python
date = "Today's date is 10-25-2023"
match = re.search(r'\d{2}-\d{2}-\d{4}', date)
if match:
    print("Found date:", match.group())
```
**Output:**
```
Found date: 10-25-2023
```

### **📌 b) Validate URL**
```python
url = "https://www.example.com"
match = re.match(r'https?://(www\.)?(\w+)(\.\w+)+', url)
if match:
    print("Valid URL:", match.group())
```
**Output:**
```
Valid URL: https://www.example.com
```

---

# **🚀 Conclusion: Regex Power in Python**
Regular Expressions are powerful for **text processing** tasks like validation, search, transformation, and extraction. Mastering these tools will make your data processing work much easier and more efficient.

---

**💡 Next Steps:**
- If you’d like, I can go deeper into **real-world applications** of regex or explore **text mining**, **log file parsing**, or **data extraction** using regex. Let me know!