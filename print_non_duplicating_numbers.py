# Initialize a dictionary to store all the number inputs
numbers = {}

# Loop 10 times using a for loop
for i in range(10):
    # -> Ask for a number input
    num = int(input(f"Enter number {i+1}: "))
    # -> If the number exists in the dictionary, increment its value by 1
    if num in numbers:
        numbers[num] += 1
    # -> Otherwise, add the number in the dictionary with a count of 1
    else:
        numbers[num] = 1

# Initialize a list to store all the unique numbers
unique_numbers = []
# Loop through the dictionary and add the number with a value of 1 to the list
for num, count in numbers.items():
    if count == 1:
        unique_numbers.append(num)
# Print the list that stores all the unique numbers