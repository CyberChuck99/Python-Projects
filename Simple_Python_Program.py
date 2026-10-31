# Simple Python Program

# Ask the user for their name
name = input("Enter your name: ")

# Ask for their favorite number (keep it a string until it's validated)
fav_input = input("Enter your favorite number: ")
while not fav_input.isdigit():
    print("Please enter a valid number.")
    fav_input = input("Enter your favorite number: ")

# Convert to an integer only after validation
fav_number = int(fav_input)

# Perform a simple calculation
double_number = fav_number * 2

# Print a greeting message and the calculated value
print(f"Hello, {name}! Your favorite number doubled is {double_number}.")
