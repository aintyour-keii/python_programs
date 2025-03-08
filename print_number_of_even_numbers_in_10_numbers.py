# Create a variable for keeping track of the number of even numbers
even_count = 0

# Using a for loop ask for a number input 10 times
for i in range(10):
    # Check if the number input is even, if it is, add 1 to the variable
    if int(input("Enter a number: ")) % 2 == 0:
        even_count += 1

# Print the number of even numbers after the loop
print(even_count)