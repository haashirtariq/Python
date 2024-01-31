# Define the addition function
def add(x, y):
    return x + y

# Define the subtraction function
def subtract(x, y):
    return x - y

# Define the multiplication function
def multiply(x, y):
    return x * y

# Define the division function
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Initialize a flag variable to control the "Exited application" message
exited = False

# Main calculator loop
while True:
    # Display the menu
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    # Get the user's input
    user_input = input(": ")

    # Check the user's choice
    if user_input == "quit":
        exited = True
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            print("Result:", add(num1, num2))
        elif user_input == "subtract":
            print("Result:", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result:", multiply(num1, num2))
        elif user_input == "divide":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input. Please try again")

# Check if the user chose to quit and then display the "Exited application" message
if exited:
    print("Exited application")
