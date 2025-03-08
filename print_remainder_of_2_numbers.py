# Ask for 2 number inputs

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if the 2nd input is 0, if it is not proceed with calculating the remainder 
if num2 != 0:
    # Calculate the remainder of the division of the two numbers using the modulus operator (%)
    remainder = num1 % num2
    # Print the remainder
    print(remainder)