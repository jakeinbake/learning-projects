# Random_Menu T
import time
run_menu = True
menu_options = [1,2,3]
menu_options[0] = "1. Current Time"
menu_options[1] = "2. Filler1"
menu_options[2] = "3. Quit"
print ("Welcome to your random menu!");print ("Your random menu has a few options to choose from!");print("Your options are: \n" + (' \n'.join(menu_options)))
while run_menu == True:
    user_selection = str(input("Which menu would you like to enter? "))
    if user_selection == '1':
        ct = time.localtime()
        current_time = time.strftime("%H:%M:%S", ct)
        print("The current time is " + current_time + " \nReturning to the menu!")
    elif user_selection == '2':
        print("Something 1")
    elif user_selection == '3':
        print ("Okay, thank you for using our menu.\nHave a great day!")
        run_menu = False
    else:
        print("You've provided an invalid selection, please try again!")
