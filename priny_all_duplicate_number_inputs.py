# Initialize a dictionary to store all the number inputs
numbers = {}
# Loop 10 times using a for loop
for _ in range(10):
    # -> Ask for a number input
    num = int(input("Enter a number: "))
    if num in numbers: # -> If the number exists in the dictionary, increment its value by 1
        numbers[num] += 1
    else: # -> Otherwise, add the number in the dictionary with a count of 1
        numbers[num] = 1

# Initialize a list to store all the duplicated numbers
duplicated_numbers = []
# Loop through the dictionary and add the number with a value of greater than 1 to the list
for num, count in numbers.items():
    if count > 1:
        duplicated_numbers.append(num)

# Print the list that stores all the numbers that was inputted more than once
print(duplicated_numbers)