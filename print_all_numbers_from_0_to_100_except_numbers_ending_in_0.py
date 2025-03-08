# using a for loop, iterate from 0 - 100
for i in range(101):
    # convert the number to string
    str_i = str(i)
    # check the last digit of the string using string slicing
    last_digit_string = str_i[-1]
    # convert the last digit to int and check if it is 0
    last_digit_int = int(last_digit_string)
    # if it is 0 continue the loop otherwise print the number
    if last_digit_int == 0:
        continue
    else:
        print(i)