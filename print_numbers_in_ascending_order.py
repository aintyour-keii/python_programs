# Initialize an empty list to store all inputted numbers
numbers = []

# Continuously ask for a number input using a while True loop
while True:
    # Check if the input is valid using try/except
    try:
        # If the input is valid append the input to the list
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        # Otherwise break out of the loop
        break

# Check if there were any valid inputs by checking on the list
if numbers:
    # If there were valid inputs, using the sort method, sort the list in ascending order
    numbers.sort()
    # Print the sorted list