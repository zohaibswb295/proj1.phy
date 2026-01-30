# proj1.phy
# 🧮 Python Calculator

A simple calculator program built using **Python**.

This project allows users to perform basic arithmetic operations through user input.

---

## 📌 Features

- Addition  
- Subtraction  
- Multiplication  
- Division  
- User-friendly menu system  
- Beginner-friendly Python code  

---

## 🛠️ Technologies Used

- Python 3

---

## ▶️ How It Works

1. The program asks the user to enter two numbers.
2. A menu is displayed with four operations:
   - 1 → Addition  
   - 2 → Subtraction  
   - 3 → Multiplication  
   - 4 → Division  
3. The user selects an option.
4. The result is displayed based on the selected operation.

---

## 💻 Code Example

```python
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))

print("1: addition")
print("2: subtraction")
print("3: multiplication")
print("4: division")

choice = input("enter your choice :(1/2/3/4)")

if choice == "1":
    print(num1 + num2)
elif choice == "2":
    print(num1 - num2)
elif choice == "3":
    print(num1 * num2)
elif choice == "4":
    print(num1 / num2)
else:
    print("invalid statement")
.  
