# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruitlist = ["apple","orange","pear"]
# TODO: Use a for loop to print each fruit in the list
for fruit in fruitlist:
    print(fruit)
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1

countdown = 5
while countdown > 0 :
    print(countdown)
    countdown-= 1
#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers

for num in range (1,11) :
    sqr = num ** 2
    print(sqr)
#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colours = ["red","blue","green","yellow","pink","orange","white","black"]
# TODO: Use a for loop to select and print 3 random colors from the list
for num1 in range(3):
    colour = random.choice(colours)
    print(colour)

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations

# TODO: Use a while loop to create a simple calculator
while True :
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    opp = input("Input operation (+, -, *, /): ")

    if opp == "+":
        result = math_operations.add(a, b)
    elif opp == "-":
        result = math_operations.subtract(a, b)
    elif opp == "*":
        result = math_operations.multiply(a, b)
    elif opp == "/":
        result = math_operations.divide(a, b)
        
    print("Result:", result)
