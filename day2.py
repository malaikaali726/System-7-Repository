# Day 2: Conditions, loops, range(), functions

# Conditions
marks = 75
if marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C")

# Loops
print("For loop:")
for i in range(1, 6):
    print(i)

print("While loop:")
count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1

# range() with step
print("Even numbers 0 to 10:")
for n in range(0, 11, 2):
    print(n)

# Functions
def add(x, y):
    return x + y

def greet(name="Malaika"):
  print("Good Morning", name)

print("Sum:", add(5, 7))
greet("Laina")
greet()