# Task 3: Student record manager that saves to a file
import json
import os

FILE_NAME = "students.json"

def load_students():
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print("Error loading file:", e)
        return {}

def save_students(students):
    try:
        with open(FILE_NAME, "w") as f:
            json.dump(students, f, indent=4)
    except OSError as e:
        print("Error saving file:", e)

def add_student(students):
    roll = input("Roll number: ").strip()
    if roll in students:
        print("This roll number already exists.\n")
        return
    name = input("Name: ").strip()
    try:
        marks = float(input("Marks: "))
    except ValueError:
        print("Marks must be a number.\n")
        return
    students[roll] = {"name": name, "marks": marks}
    save_students(students)
    print("Student added.\n")

def view_students(students):
    if not students:
        print("No records found.\n")
        return
    print("\n{:<10} {:<20} {:<8}".format("Roll", "Name", "Marks"))
    print("-" * 40)
    for roll, info in students.items():
        print("{:<10} {:<20} {:<8}".format(roll, info["name"], info["marks"]))
    print()

def update_student(students):
    roll = input("Roll number of the student to update: ").strip()
    if roll not in students:
        print("Record not found.\n")
        return
    try:
        marks = float(input("New marks: "))
    except ValueError:
        print("Marks must be a number.\n")
        return
    students[roll]["marks"] = marks
    save_students(students)
    print("Record updated.\n")

def delete_student(students):
    roll = input("Roll number of the student to delete: ").strip()
    if roll not in students:
        print("Record not found.\n")
        return
    del students[roll]
    save_students(students)
    print("Record deleted.\n")

def main():
    students = load_students()
    while True:
        print("1. Add student")
        print("2. View all students")
        print("3. Update marks")
        print("4. Delete student")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()