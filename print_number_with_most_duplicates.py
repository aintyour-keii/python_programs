# Initiate a dictionary to store all inputted numbers
numbers = {}
# Create an infinite loop using a while True loop
while True:
    # Inside the loop:
    # Using try/except block to catch any potential errors
    try:
        # Ask for a number input
        num = int(input("Enter a number: "))
        if num in numbers: # If it is a valid input, check if it is in the dictionary and add one to its value
            numbers[num] += 1
        else: # otherwise add it to the dictionary with a value of 1
            numbers[num] = 1
    except ValueError:
        # If the input is invalid break out of the loop
        break

# Initiate a variable to store the input with the most number of repetition
# Loop throught the dictionary and identify the input with the most number of repetition
# Print the variable that stores the input with the most number of repetition