# Initialize an empty list to store all numbers to be displayed
numbers_to_be_displayed = []
# Initialize an empty set to store all seen inputs
seen_inputs = set()

# Loop through 10 times:
for _ in range(10):
    # -> Ask the user for a number input
    num = int(input("Enter a number: "))
    # -> Check if the input has yet to be seen
    if num not in seen_inputs:
    # -> Append the input to the list
        numbers_to_be_displayed.append(num)
    # -> Add the input to the set
        seen_inputs.add(num)

# Print the list
print(numbers_to_be_displayed)