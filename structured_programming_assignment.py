
# Structured Programming Assignment Solutions

# Question One (6 Marks)
# Differentiate Between Assigning and Declaring a variable, giving practical Examples of Each

# In Java (Declaration):
# int age;  // Declaration

# In Python (Assignment and Declaration):
age = 25  # Assignment (and declaration)
name = "John"  # Declares and assigns

# Question Two (4 Marks)
# Given the code:
age = "8"
length = "56.90"
height = "34.09944"

# Convert to correct datatypes
age = int(age)
length = float(length)
height = float(height)

# Now:
# age is an int → 8
# length is a float → 56.90
# height is a float → 34.09944

# Question Three (10 Marks)
# Python program using if statements to assign grades based on user input

mark = input("Enter your mark (0 - 100): ")

try:
    mark = float(mark)

    if mark < 0 or mark > 100:
        print("Invalid mark! Please enter a value between 0 and 100.")
    elif mark <= 50:
        print("Grade: F")
    elif mark <= 64:
        print("Grade: C")
    elif mark <= 79:
        print("Grade: B")
    elif mark <= 90:
        print("Grade: A")
    else:
        print("Grade: A+")
except ValueError:
    print("Invalid input! Please enter a numeric value.")
