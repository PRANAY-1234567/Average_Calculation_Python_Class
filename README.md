# 🔢 Average Calculation Using Python Class

## 📌 Description

This Python program demonstrates how to calculate the **average of three numbers** using a class. It uses a constructor to initialize values and a method to perform the calculation.

---

## 🚀 Features

* Uses a class `Numbers`
* Initializes values using constructor (`__init__`)
* Calculates average of three numbers
* Displays the result

---

## 🛠️ How It Works

1. A class `Numbers` is created.
2. The constructor initializes three numbers:

   * `n1 = 14`
   * `n2 = 62`
   * `n3 = 53`
3. The method `average()`:

   * Adds all three numbers
   * Divides by 3 to calculate average
4. The object `obj` calls the method to display the result.

---

## 💻 Code

```python id="k2ps9m"
class Numbers:
    def __init__(self):
        self.n1 = 14
        self.n2 = 62
        self.n3 = 53

    def average(self):
        a = (self.n1 + self.n2 + self.n3) / 3.0
        print("Average :", a)


# Main program
obj = Numbers()
obj.average()
```

---

## ▶️ Example Output

```id="q8d1xv"
Average : 43.0
```

---

## 📚 Concepts Used

* Class and Object
* Constructor (`__init__`)
* Instance variables
* Arithmetic operations

---

## 🎯 Use Case

This program helps beginners understand:

* How to use constructors to initialize data
* How to perform calculations inside a class

---

## 🔧 Future Improvements

* Take input from user instead of fixed values
* Calculate average of more than 3 numbers
* Return the value instead of printing
* Add methods for sum, max, min

---

## 📄 License

This project is open-source and free to use.

<img width="730" height="846" alt="image" src="https://github.com/user-attachments/assets/c8ee04d6-2ce4-4669-becd-7206a7f04e24" />
