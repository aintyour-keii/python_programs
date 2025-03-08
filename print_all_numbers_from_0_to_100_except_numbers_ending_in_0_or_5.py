# Using a for loop, iterate to 0 - 100 (inclusive)
for i in range(101):
    # Convert the number to string
    str_i = str(i)
    # Get the last character of the string
    last_char = str_i[-1]
    # Check if the last character of the string is not "0" or "5"
    if last_char not in ["0", "5"]:
    # If the last character of the string is not "0" or "5", print the number
        print(i)