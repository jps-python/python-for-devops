Let's create a **real-world simple example** of a class in Python. We will model a **Bank Account** system. This example demonstrates how a class can represent a bank account and include attributes like balance and methods to perform operations like depositing and withdrawing money.

### **Real-World Example: Bank Account Class**

In this example:
- We'll have a class named `BankAccount`.
- Each `BankAccount` object will have attributes like `account_holder` and `balance`.
- We will define methods to:
  - Deposit money into the account.
  - Withdraw money from the account.
  - Display the account balance.

#### Code Example:

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        # Initializing the account holder's name and initial balance
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        # Method to deposit money into the account
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be greater than zero.")
    
    def withdraw(self, amount):
        # Method to withdraw money from the account
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be greater than zero.")
    
    def get_balance(self):
        # Method to display the current balance
        return self.balance

# Creating an instance of BankAccount for a customer
account1 = BankAccount("John Doe", 1000)

# Display initial balance
print(f"Initial balance: ${account1.get_balance()}")

# Deposit some money
account1.deposit(500)

# Withdraw some money
account1.withdraw(300)

# Try to withdraw more than the balance
account1.withdraw(1500)

# Display final balance
print(f"Final balance: ${account1.get_balance()}")
```

### **Explanation of the Code:**

1. **`__init__(self, account_holder, initial_balance=0)`**:
   - This is the constructor method that initializes the object. It accepts two parameters: `account_holder` and `initial_balance`. The `initial_balance` is optional and defaults to `0` if not provided.

2. **`deposit(self, amount)`**:
   - This method allows depositing money into the account. If the `amount` is valid (positive), it adds the amount to the balance. It also prints a message showing the updated balance.
   - If the amount is less than or equal to zero, it displays an error message.

3. **`withdraw(self, amount)`**:
   - This method allows withdrawing money from the account. It checks if the withdrawal is valid (positive and less than or equal to the balance). If the withdrawal is successful, it subtracts the amount from the balance.
   - If the withdrawal amount exceeds the balance or is invalid, it shows an error message.

4. **`get_balance(self)`**:
   - This method returns the current balance of the account.

---

### **Output:**

```plaintext
Initial balance: $1000
Deposited $500. New balance is $1500.
Withdrew $300. New balance is $1200.
Insufficient funds.
Final balance: $1200
```

### **Key Points Demonstrated:**

1. **Object Creation**: We created an object of the `BankAccount` class with an initial balance of $1000 for `John Doe`.
2. **Attributes**: `account_holder` and `balance` are instance attributes.
3. **Methods**: The `deposit`, `withdraw`, and `get_balance` methods allow interaction with the object's data.
4. **Validation**: We validated inputs to ensure that deposits and withdrawals are valid (i.e., positive amounts, sufficient balance for withdrawals).
5. **Real-World Concept**: This example represents a **Bank Account**—something that is simple and easy to relate to, and shows how we can manage and manipulate an object's state through methods.

---

This is a simple example of how classes in Python are used to model real-world systems. It demonstrates **encapsulation**, where the account balance is protected and can only be modified through methods, providing a safe interface to interact with the object's data.