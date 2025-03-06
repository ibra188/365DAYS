"""
Variables and Data Types
A variable is like a box where you store things. You give it a name, and it keeps your stuff safe.
"""

name = "Anna" # This is a string (text)
age = 25 # This is an interger (whole number)
height = 1.65 # This is a float (number with decimals)
job = "Recuiter" #This is a string  (text)
married = False # This is a boolean (True or False)

name = input("What is your name?")
print("Hello, " + name + "!")

"""
Operators
Operators are tools to do math or compare things:
"""

# Math Operators
x = 5
y = 3
print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division
print(x % y) # Modulus (remainder)
print(x ** y) # Exponentiation (power)

# Comparison Operators
print( 10 > 5) # greater than
print(10 < 5) # less than
print(10 >= 5) # greater than or equal to
print(10 <= 5) # less than or equal to
print(10 == 5) # equal to
print(10 != 5) # not equal to

# Control Flow
"""
Conditional Statements (if, elif, else)
Imagine you're playing a game. If you score above 90, you win! Let’s code that logic:
"""
score = int(input("Enter your score: ")) # convert input to interger
if score > 90:
    print("you win the game!")
elif score == 90:
    print("you barley win the game!")
else:
    print("you lose the game!")

"""
Loops (for, while)
Loops are for repeating things!
"""
# For Loop:
for i in range(10):
    print(i) # prints 0 to 9

#While Loop:
count = 0
while count < 10:
    print(count)
    count += 1 # increment count by 1

# Break and Continue Statements
for i in range(10):
    if i == 5:
        break # stops the loop
    print(i)

for i in range(10):
    if i == 5:
        continue # skips the current iteration
    print(i)

"""
Data Structures
Lists (A collection of items, like a shopping list)
Lists can hold anything—numbers, words, or even other lists!
"""
