# **🚀 Advanced Regex & JSON/XML Handling in Python**

Let’s dive deep into **Regular Expressions (Regex)** and **handling JSON/XML data** in Python. These skills are essential for data parsing, validation, and extraction.

---

# **🔹 1. Mastering Regular Expressions (Regex)**
Python’s `re` module provides **powerful** tools for working with regular expressions.

### **📌 a) Importing Regex Module**
```python
import re
```

---

## **🔸 b) Common Regex Patterns**
| **Pattern**    | **Description**                     | **Example Match**  |
|---------------|---------------------------------|----------------|
| `\d`         | Any digit (0-9)                 | `"abc123" → 123` |
| `\D`         | Any non-digit                   | `"abc123" → abc` |
| `\w`         | Any word character (a-z, A-Z, 0-9, _) | `"Python_3"` |
| `\W`         | Any non-word character          | `"Hello! 123"` |
| `\s`         | Any whitespace (space, tab, newline) | `"Hello World"` |
| `\S`         | Any non-whitespace character    | `"Hello_World"` |
| `.`          | Any single character (except newline) | `"h.t"` → `hat, hit` |
| `^`          | Start of a string               | `"^hello"` → Matches `"hello world"` |
| `$`          | End of a string                 | `"world$"` → Matches `"hello world"` |

---

## **🔸 c) Search for Patterns**
### **✔ Find a Match**
```python
text = "My email is example@gmail.com"
match = re.search(r"\S+@\S+", text)  # Find email pattern
print(match.group())  # Output: example@gmail.com
```

---

### **✔ Find All Matches**
```python
text = "Emails: test1@example.com, test2@gmail.com"
emails = re.findall(r"\S+@\S+", text)
print(emails)  # Output: ['test1@example.com', 'test2@gmail.com']
```

---

### **✔ Replace Substring**
```python
text = "My number is 123-456-7890"
formatted_text = re.sub(r"\d{3}-\d{3}-\d{4}", "XXX-XXX-XXXX", text)
print(formatted_text)  # Output: "My number is XXX-XXX-XXXX"
```

---

### **✔ Extract Numbers**
```python
text = "Order ID: 56789, Amount: $123.45"
numbers = re.findall(r"\d+", text)
print(numbers)  # Output: ['56789', '123', '45']
```

---

# **🔹 2. Working with JSON in Python**
JSON (JavaScript Object Notation) is widely used for APIs, configuration files, and data storage.

### **📌 a) Importing JSON Module**
```python
import json
```

---

### **🔸 b) Convert JSON String to Python Dictionary**
```python
json_data = '{"name": "Alice", "age": 25, "city": "New York"}'

# Parse JSON
data = json.loads(json_data)
print(data["name"])  # Output: Alice
```

---

### **🔸 c) Convert Python Dictionary to JSON String**
```python
person = {
    "name": "Bob",
    "age": 30,
    "skills": ["Python", "Django", "DevOps"]
}

json_string = json.dumps(person, indent=4)
print(json_string)
```
**Output:**
```json
{
    "name": "Bob",
    "age": 30,
    "skills": ["Python", "Django", "DevOps"]
}
```

---

### **🔸 d) Read JSON from a File**
```python
with open("data.json", "r") as file:
    data = json.load(file)
    print(data["city"])  # Access a value from JSON
```

---

### **🔸 e) Write JSON to a File**
```python
person = {"name": "Charlie", "age": 28}

with open("output.json", "w") as file:
    json.dump(person, file, indent=4)
```

---

# **🔹 3. Working with XML in Python**
XML (Extensible Markup Language) is widely used in web services and data exchange.

### **📌 a) Importing XML Library**
Python provides the built-in `xml.etree.ElementTree` for handling XML.
```python
import xml.etree.ElementTree as ET
```

---

### **🔸 b) Parse XML Data**
```xml
<data>
    <person>
        <name>Alice</name>
        <age>25</age>
        <city>New York</city>
    </person>
</data>
```

```python
xml_data = """<data>
    <person>
        <name>Alice</name>
        <age>25</age>
        <city>New York</city>
    </person>
</data>"""

root = ET.fromstring(xml_data)
name = root.find(".//name").text  # Extract <name>
print(name)  # Output: Alice
```

---

### **🔸 c) Read XML from a File**
```python
tree = ET.parse("data.xml")
root = tree.getroot()

for person in root.findall("person"):
    name = person.find("name").text
    print(name)
```

---

### **🔸 d) Create and Write XML File**
```python
root = ET.Element("data")
person = ET.SubElement(root, "person")

ET.SubElement(person, "name").text = "Charlie"
ET.SubElement(person, "age").text = "30"

tree = ET.ElementTree(root)
tree.write("output.xml")
```

---

# **🔹 4. JSON vs XML: When to Use?**
| **Feature** | **JSON** | **XML** |
|------------|---------|---------|
| Readability | Easy to read | Verbose |
| Parsing | Faster | Slower |
| Support | Widely used in APIs | Used in legacy systems |
| Schema Support | No built-in schema | Strong schema support |

---

# **🚀 What’s Next?**
Do you want to explore **API requests, web scraping, or log analysis using regex?** Let me know!