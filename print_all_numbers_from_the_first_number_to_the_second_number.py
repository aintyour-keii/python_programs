# Ask for 2 number inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Identify the start and end (inclusive) by their value
start = min(num1, num2)
# start - smaller number and end - larger number
end = max(num1, num2)
# Print the range of numbers from start to end (inclusive)
for i in range(start, end + 1):
    print(i)