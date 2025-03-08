# Ask for the first number input
first_number = int(input("Enter the first number: "))
# Create a variable to store the sum of the remaining 9 numbers
sum_remaining_numbers = 0
# Using a for loop, ask for a number input 9 times
for i in range(9):
    num = int(input("Enter a number: "))
    # Add each number to the sum variable
    sum_remaining_numbers += num

# Calculate the difference of the first number and the sum of the remaining 9 numbers
result = first_number - sum_remaining_numbers

# Print the result
print(result)