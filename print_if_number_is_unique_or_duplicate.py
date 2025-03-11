# Initialize an empty set to keep track of unique numbers
unique_numbers = set()
# Using a while True loop
while True:
    # -> try asking for a valid number input
    try:
        num = int(input("Enter a number: "))
        # -> if the input is valid
        #   -> check if the number is the set
        #   -> if the number is found in the set print "Duplicate"
        #   -> otherwise, print "Unique" and add it to the set
    except ValueError:
        # -> if the input is invalid, break out of the loop and stop the program
        break