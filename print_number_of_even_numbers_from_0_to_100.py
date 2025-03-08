# initialize the "even_count" variable to 0
even_count = 0

# using for loop, iterate over the numbers from 0 to 100
for i in range(101):
    # check if the number is even by using the modulus operator (%)
    if i % 2 == 0:
    # if the number is even, increment the "even_count" variable by 1
        even_count += 1

# print the "even_count" variable after the loop finishes