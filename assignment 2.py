# Start of Program

# This function greets the user by name
def greet_user():
    # Prompt the user to enter their name
    name = input("Enter your name: ")
    # Print a personalized welcome message with the user's name
    print("Welcome, " + name)

# This function checks if a number is even or odd
def check_even_odd(number):
    # Check if the number is divisible by 2
    if number % 2 == 0:
        print("Even")  # Print "Even" if the number is divisible by 2
    else:
        print("Odd")   # Print "Odd" if the number is not divisible by 2

# Main program execution
greet_user()  # Call the function to greet the user
# Prompt the user to enter a number and convert it to an integer
number = int(input("Enter a number: "))
check_even_odd(number)  # Call the function to check even/odd status

# End of Program
