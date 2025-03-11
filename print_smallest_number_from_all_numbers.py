# Initialize a variable to None, this will store the lowest number value
lowest_number = None
# Continously ask for number input using a while True loop
while True:
    # Check if the number input is valid
    try:
        num = int(input("Enter a number: "))
        # If the input is a valid
        # Check if the variable is None or the input is less than the variable
        if lowest_number is None or num < lowest_number:
            # If so, update the variable's value to the input
            lowest_number = num

    # If the input is invalid, break out of the loop
    except ValueError:
        break

# Check if the variable is not "None", if so print the variable's value
if lowest_number is not None:
    print(lowest_number)