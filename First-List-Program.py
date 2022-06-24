# First program
print("Hello World!")
print("Lets build a list!")
# Establish a count value
count = 0
# Creating our empty list
data = []
# How many items should be in our list?
num_input = int(input("How many items should be in our list? "))
# Create a loop to take user input based on how many items they'd like in their list
while count < num_input:
    # Take user input 
    user_input = input("What number should we add to your list? ")
    # Add that user input to our list
    data.append(user_input) 
    # Increment our count by one to progress the loop
    count += 1
else:
    print("You've finished inputting your values! You entered: ", data)