# Initialize a list to store all inputted numbers
numbers = []
# Create an infinite loop using a while True statement
while True:
    # Inside the loop, ask the user for a number with a try/except block to handle invalid inputs
    # If the input is valid then add the number to the list
    try: 
        num = int(input("Enter a number: "))
        numbers.append(num)
    # Otherwise, break out of the while loop
    except ValueError:
        break

# Calculate the average by using the sum() method to find the sum of all the numbers and len() to find the number of elements in the list
# Print the average