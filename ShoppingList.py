# Shopping List That Calculates Total Cost of your order and then outputs it cleanly
import string
print("Hello! Lets put together your shopping list!")
# Create an empty shopping list
shoppingList = []
# Create an empty list of prices
listPrice = []
# Set a counter to 0 - not sure if we'll ever use this.. initially planned to use it to remove data upon bad answer
count = 0
# shouldContinue is defaulted to True
shouldContinueValue = True
# Loop determining how long to continue accepting input
while shouldContinueValue == True:
    # Input item name
    shoppingListInput = input("What are we buying? ")
    # Add item to list
    shoppingList.append(shoppingListInput)
    # Input item cost
    listPriceInput = int(input("How much does that cost? "))
    # Add cost to list
    listPrice.append(listPriceInput)
    # Force us into the loop below to validate input
    badAnswer = True
    while badAnswer == True:
         # Ask user if they're done adding to their list, store answer
        shouldContinue = input("Is that everything? Y/N ")
        shouldContinue = shouldContinue.lower()
        if shouldContinue == 'y' or shouldContinue == 'yes': # If true, end this loop
            shouldContinueValue = False # set shouldContinueValue == False to break out of loop we're nested in
            print("Okay, all done then!")
            break
        elif shouldContinue == 'n' or shouldContinue == 'no': # If true, break out of this loop and return to loop we're nested in
            shouldContinueValue = True # Re-set shouldContinueValue == True to break out of this loop but remain in nested loop
            print("Okay, lets keep going!")
            count += 1
            break  
        else: # Otherwise, 'bad data!' repeat the question.
            print("You've provided invalid input, please use Y/N format!")
            shouldContinueValue = True
            badAnswer = True
            continue
print("Okay, your list is finished!")
shoppingListClean =(', '.join(shoppingList)) # Strip brackets from list output so it's 'cleaner'
print("The items in your list were: ", shoppingListClean)
print("The total cost of those items were: $",sum(listPrice)) # Sum values in listPrice to get order total