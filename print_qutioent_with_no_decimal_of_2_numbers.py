# Ask for 2 number inputs

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if the 2nd input is not 0, if it is not, proceed with floor division
if num2 != 0:
    # Using the built-in floor division, divide the 1st input by the 2nd input
    result = num1 // num2
    # Print the result of the division
    print(result)