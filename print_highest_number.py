# Initialize a variable that stores the highest number
highest_number = None
# Create an infinite loop using a while True statement
while True:
# Inside the loop, use a try/except block to handle potential errors
# Try asking the user for a number, convert it to an integer
    try: # If the user enters an inter value, if the variable is not empty or if the inputted number is higher than the current highest number, update the variable
        num = int(input("Enter a number: "))
        
    except ValueError: # If the user enters a non-integer value, catch the ValueError and break out of the while loop
        break
    
# Print the variable that store the highest number