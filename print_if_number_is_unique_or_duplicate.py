# Initialize an empty set to keep track of unique numbers
unique_numbers = set()
# Using a while True loop
while True:
    # -> try asking for a valid number input
    try:
        num = int(input("Enter a number: "))
        # -> if the input is valid
        #   -> check if the number is the set
        if num in unique_numbers:
            #   -> if the number is found in the set print "Duplicate"
            print("Duplicate")
        else:
            #   -> otherwise, print "Unique" and add it to the set
            print("Unique")
            unique_numbers.add(num)
            
    except ValueError:
        # -> if the input is invalid, break out of the loop and stop the program
        break