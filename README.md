
# 🔐 Password Generator – Python

A simple yet powerful **Password Generator** built using Python. This program allows users to generate secure, randomized passwords based on their preferred number of **letters**, **numbers**, and **symbols**. It includes built-in **error handling**, **input validation**, and **random shuffling** to ensure strong, unpredictable password creation.

---

## 🚀 Features

### ✅ Customizable Password Structure

Users can choose:

* Number of **letters** (a–z, A–Z)
* Number of **digits** (0–9)
* Number of **symbols** (! @ # $ % & * + - _)

### 🔄 Randomized & Secure

* Uses Python’s built-in **`random`** module to generate pseudo-random characters.
* Final password structure is **shuffled** to maximize unpredictability.

### ⚠️ Error Handling Included

* Prevents **negative inputs**.
* Limits password length to **maximum 100 characters**.
* Ensures password length is not zero.
* Catches unexpected errors and `KeyboardInterrupt`.

### 🧪 Input Validation

The program checks:

* That all values are positive
* Combined length > 0
* Password length ≤ 100

### 🎯 User-Friendly Interface

Clean and simple console-based UI with clear instructions.

---

## 📌 How It Works

1. Prompts the user to enter:

   * Number of letters
   * Number of numbers
   * Number of symbols

2. Generates the required characters using:

   * `random.choice()`

3. Appends all characters to a temporary string.

4. Converts the string to a list and **shuffles it** using `random.shuffle()`.

5. Joins the list into a final strong password.

6. Prints the generated password.

---

## 🛠️ Technologies Used

* **Python 3.x**
* **random module** (built-in)

---

## 📷 Sample Output


Welcome to password generator

Please enter how many LETTERS required in your password : 4
Please enter how many NUMBERS required in your password : 3
Please enter how many SYMBOLS required in your password : 2

Your strong password is:  @b7A1f+2

---

## 📄 Code Highlights

* Character lists for letters, digits, and special symbols
* Looping structures for character generation
* List conversion & shuffling for randomness
* Exception handling for robust execution

