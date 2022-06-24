
# Shopping List That Calculates Total Cost
print("Hello! Lets put together your shopping list!")
# Create an empty shopping list
shoppingList = []
# Create an empty list of prices
listPrice = []
# Set a counter to 0
count = 0
# shouldContinue is defaulted to True
shouldContinueValue = True
# Loop determining how long to take input for
while shouldContinueValue == True:
    # Input item name
    shoppingListInput = input("What are we buying? ")
    # Add item to list
    shoppingList.append(shoppingListInput)
    # Input item cost
    listPriceInput = int(input("How much does that cost? "))
    # Add cost to list
    listPrice.append(listPriceInput)
    count += 1
    # Ask user if they're done adding to their list, store answer
    shouldContinue = input("Is that everything? Y/N ")
    shouldContinue = shouldContinue.lower()
    # Check shouldContinue input
    
    if shouldContinue == 'y':
        shouldContinueValue = False
        print("Okay, all done then!")
    elif shouldContinue == 'n':
        shouldContinueValue = True
        print("Okay, lets keep going!")
    else:
        print("You've provided invalid input, please use Y/N format!")
        shouldContinueValue = True

print("Okay, your list is finished!")
shoppingListClean =(', '.join(shoppingList))
print("The items in your list were: ", shoppingListClean)
print("The total cost of those items were: $",sum(listPrice))

        
    