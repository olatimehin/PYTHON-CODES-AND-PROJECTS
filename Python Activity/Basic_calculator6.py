'''Problem Statement:
Create a Basic Calculator that can do Addition, Subtraction, Multiplication and Division in Python.

Questions:
- How to create Choices for the user?
- How the user input two numbers?
- How can you add your define functions inside your If-else statements?
- How do stop the calculations at a certain part?
- How do you cope with this when a user will type a invalid input?'''

# Define a function to perform addition of two numbers
# Define a function to perform subtraction of two numbers
# Define a function to perform multiplication of two numbers
# Define a function to perform division of two numbers
    # Return the result of division
    # Note: This code does not handle division by zero
# Print the options for the user to select an operation
# Start an infinite loop to repeatedly prompt the user for input until they choose to exit
    # Prompt the user to input a choice for the operation
    # Check if the user's choice is one of the valid options (1, 2, 3, 4)
         # Ask the user to input two numbers for the calculation
         # Handle invalid inputs (i.e., when the user does not enter a valid number)
             # Continue to the next iteration of the loop
        # Perform the corresponding operation based on the user's choice
        # Ask the user if they want to perform another calculation
        # If the user chooses "no", break out of the loop and end the program
    # If the user enters an invalid option, display an error message
 
# First method        
def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    
    return x / y


print("SELECT OPERATION")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide") 


while True:
    
    
    choice = input("ENTER CHOICE: ")
    
    
    if choice in ("1", "2", "3", "4"):
        try: 
           
            num1 = float(input("Enter first number: "))  #what is the excess of try and except
                                                            # what is the excess of please enter a number btw 1-4
            num2 = float(input("Enter second number: "))
        
        
        except ValueError:
            print("INVALID INPUT. \nPlease enter a valid number.")
            continue 

        
        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))
            
        elif choice == "2":
            print(num1, "-", num2, "=", substract(num1, num2))
            
        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))
            
        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))  
            
        
        new_calculation = input("Do you want to do another calculation (yes/no): ")
        
        
        if new_calculation.lower() == "no":
            break

    
    else:
        print("Invalid Input")



# ALTERNATIVE ANSWER(This second code Explicit handling for division by zero,also "Exit" option provided, allowing the user to terminate the calculator smoothly
# it allow the user pressing 5 for exit immediately if user decide to exit without choosing any number)   
        
# Define functions for the basic operations
# Create a loop to continuously ask the user for input
    # Display options for the user to choose from
    # Take user input for operation choice
    # Exit condition
    # Ensure valid input for operation choice
        # Take input from the user for two numbers
    # Perform the selected operation using if-else

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


while True:
    
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    
    choice = input("Enter choice(1/2/3/4/5): ")

    
    if choice == '5':
        print("Exiting the calculator.")
        break

    
    if choice in ['1', '2', '3', '4']:
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        
        if choice == '1':
            print(f"The result of addition: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"The result of subtraction: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result of multiplication: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result of division: {num1} / {num2} = {divide(num1, num2)}")

    else:
        print("Invalid input! Please enter a valid option.")
