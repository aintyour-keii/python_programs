# initialize the "odd_count" variable to 0
odd_count = 0
# loop through 10 times
for i in range(10):
    # in each iteration, ask for a number input
    num = int(input("Enter a number: "))
    # check if the input is odd if it is add 1 to the "odd_count" variable
    if num % 2 != 0:
        odd_count += 1

# print the "odd_count" variable