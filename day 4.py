# Day 4: File handling, exceptions, modules, basic OOP
import math

# File handling
with open("notes.txt", "w") as f:
    f.write("Pehli line\n")
    f.write("Doosri line\n")

with open("notes.txt", "r") as f:
    print("File content:")
    print(f.read())

# Exceptions
try:
    number = int("abc")
except ValueError:
    print("Error: Yeh number nahi hai")
finally:
    print("Exception handling complete")

# Modules
print("Square root of 16:", math.sqrt(16))

# Basic OOP
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Mera naam {self.name} hai aur meri umar {self.age} saal hai.")

s1 = Student("Laina", 20)
s1.introduce()