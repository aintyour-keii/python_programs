# Ask for 2 float inputs

num1 = float(input("Enter the first number(decimal allowed): "))
num2 = float(input("Enter the second number(decimal allowed): "))

# Check if the 2nd input is not 0, if it is 0 then return otherwise proceed with division
# Divide the 2 inputs
# Print the result
if num2 != 0:
    result = num1/num2
    print(result)