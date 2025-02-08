### **Regular Expressions (re) in Python**

Regular expressions (often abbreviated as **regex**) are a powerful tool for matching and manipulating strings based on patterns. Python provides a module called `re` for working with regular expressions.

With `re`, you can search, match, and manipulate strings efficiently using regular expressions.

---

### **Basic Operations with `re` Module**

Here's an overview of the basic operations and functions provided by the `re` module:

#### 1. **re.match()**
The `match()` function checks if the regular expression pattern matches the beginning of the string.

```python
import re

pattern = r'^hello'
text = 'hello world'
result = re.match(pattern, text)

if result:
    print("Match found:", result.group())
else:
    print("No match")
```

**Explanation**: `^` indicates the start of the string. The pattern `^hello` matches only if the string starts with "hello".

---

#### 2. **re.search()**
The `search()` function searches the entire string for the first location where the regular expression matches.

```python
import re

pattern = r'world'
text = 'hello world'
result = re.search(pattern, text)

if result:
    print("Search found:", result.group())
else:
    print("No match")
```

**Explanation**: `re.search()` scans the entire string to find the first match of the pattern.

---

#### 3. **re.findall()**
The `findall()` function returns all non-overlapping matches of the regular expression in a string as a list.

```python
import re

pattern = r'\d+'  # matches one or more digits
text = 'There are 123 apples and 456 oranges'
matches = re.findall(pattern, text)

print("Matches:", matches)
```

**Output**: 
```
Matches: ['123', '456']
```

**Explanation**: The pattern `\d+` matches one or more digits, and `findall()` returns a list of all matching substrings.

---

#### 4. **re.sub()**
The `sub()` function replaces the occurrences of the pattern in the string with a replacement string.

```python
import re

pattern = r'\d+'
text = 'There are 123 apples and 456 oranges'
new_text = re.sub(pattern, 'X', text)

print("New text:", new_text)
```

**Output**:
```
New text: There are X apples and X oranges
```

**Explanation**: The pattern `\d+` matches digits and replaces them with 'X'.

---

#### 5. **re.split()**
The `split()` function splits the string into a list at each match of the regular expression.

```python
import re

pattern = r'\s+'  # matches one or more spaces
text = 'Hello   World   Python'
result = re.split(pattern, text)

print("Split result:", result)
```

**Output**:
```
Split result: ['Hello', 'World', 'Python']
```

**Explanation**: The pattern `\s+` matches one or more spaces, so the string is split by spaces.

---

### **Common Regular Expression Patterns**

- `.`: Matches any character except a newline.
- `^`: Matches the beginning of the string.
- `$`: Matches the end of the string.
- `\d`: Matches any digit, equivalent to `[0-9]`.
- `\D`: Matches any non-digit.
- `\w`: Matches any alphanumeric character (letters and digits) and underscore (`_`).
- `\W`: Matches any non-alphanumeric character.
- `\s`: Matches any whitespace character (spaces, tabs, newlines).
- `\S`: Matches any non-whitespace character.
- `+`: Matches one or more occurrences of the preceding element.
- `*`: Matches zero or more occurrences of the preceding element.
- `?`: Matches zero or one occurrence of the preceding element.
- `{n}`: Matches exactly `n` occurrences of the preceding element.
- `{n,}`: Matches `n` or more occurrences of the preceding element.
- `{n,m}`: Matches between `n` and `m` occurrences of the preceding element.
- `[]`: Matches any character inside the square brackets.
- `|`: Matches either the pattern before or after the pipe.

---

### **Examples of Regular Expressions**

#### 1. **Validate Email Address**

```python
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        print(f"'{email}' is a valid email")
    else:
        print(f"'{email}' is not a valid email")

# Test
validate_email("test@example.com")
validate_email("invalid-email.com")
```

**Explanation**: The regex pattern checks for a valid email format (letters, digits, special characters, `@`, and domain).

---

#### 2. **Extract Phone Numbers**

```python
import re

text = "Contact us at 123-456-7890 or 987-654-3210"
pattern = r'\d{3}-\d{3}-\d{4}'  # Matches phone numbers in the format 123-456-7890

matches = re.findall(pattern, text)
print("Phone numbers:", matches)
```

**Output**:
```
Phone numbers: ['123-456-7890', '987-654-3210']
```

**Explanation**: The pattern `\d{3}-\d{3}-\d{4}` matches phone numbers in the specific format of 3 digits, a hyphen, 3 digits, another hyphen, and 4 digits.

---

#### 3. **Find and Replace Dates**

```python
import re

text = "The event is scheduled for 12/10/2023 and 15/12/2023."
pattern = r'(\d{2})/(\d{2})/(\d{4})'  # Matches dates in the format dd/mm/yyyy

new_text = re.sub(pattern, r'\3-\2-\1', text)  # Replaces dates in yyyy-mm-dd format
print(new_text)
```

**Output**:
```
The event is scheduled for 2023-10-12 and 2023-12-15.
```

**Explanation**: The regex matches dates and rearranges them from `dd/mm/yyyy` to `yyyy-mm-dd` format using backreferences (`\1`, `\2`, `\3`).

---

### **Advanced Features**

#### 1. **Group Matching**

You can group parts of the pattern using parentheses to capture specific sub-patterns.

```python
import re

pattern = r'(\d{3})-(\d{2})-(\d{4})'  # Capture groups for phone number or date
text = 'My number is 123-45-6789'

match = re.match(pattern, text)
if match:
    print(f"Area Code: {match.group(1)}")
    print(f"Prefix: {match.group(2)}")
    print(f"Line Number: {match.group(3)}")
```

**Explanation**: Groups allow you to isolate and reference parts of the match, like extracting different parts of a phone number.

---

#### 2. **Lookahead and Lookbehind**

Lookahead and lookbehind assertions allow you to match patterns based on what comes before or after the match, without including it in the result.

```python
import re

text = "My email is test@example.com"
# Positive lookahead: Match "test" only if it's followed by "@"
pattern = r'test(?=@)'

match = re.search(pattern, text)
if match:
    print(f"Found: {match.group()}")
```

**Explanation**: The lookahead `(?=@)` checks if the pattern "test" is followed by the "@" symbol, but it doesn't include "@" in the match.

---

### **Conclusion**

Regular expressions (`re` module) in Python are a powerful tool for string manipulation. Here’s a quick summary of what you can do with regular expressions in Python:

- **Pattern matching**: Check if a string matches a specific pattern.
- **Text extraction**: Use `findall()` or `match()` to extract specific parts of the text.
- **Text replacement**: Use `sub()` to replace parts of a string.
- **Text splitting**: Use `split()` to break a string into parts based on a pattern.
- **Advanced matching**: Use lookahead/lookbehind and group matching for more sophisticated operations.

Regular expressions are a must-know skill for any Python developer, especially in DevOps and data processing tasks, where text manipulation and pattern matching are frequently required.