# Day 3: Lists, tuples, dictionaries, sets

# Lists (ordered, changeable)
fruits = ["apple", "mango", "banana"]
fruits.append("orange")
fruits.remove("banana")
print("Fruits:", fruits)
print("First fruit:", fruits[0])

# Tuples (ordered, unchangeable)
coordinates = (33.6, 73.0)
print("Coordinates:", coordinates)

# Dictionaries (key-value pairs)
student = {"name": "malaika", "age": 20, "course": "BSCS"}
student["city"] = "Lahore"
print("Student:", student)
print("Course:", student["course"])

# Sets (unique values, unordered)
numbers = {1, 2, 2, 3, 3, 3}
print("Unique numbers:", numbers)
numbers.add(4)
print("After adding 4:", numbers)