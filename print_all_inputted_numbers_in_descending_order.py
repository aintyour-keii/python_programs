# Initialize a list to store all inputted numbers
numbers = []
# Create an infinite loop using a while True statement
while True:
    # Inside the loop, ask the user to input a number with a try/except block to handle invalid inputs
    try: # If the input is valid, append the input to the list
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError: # Otherwise, break out of the while loop
        break

# Sort the list using the sort() function with the reverse=True argument to sort in descending order
numbers.sort(reverse=True)

# Print the sorted list