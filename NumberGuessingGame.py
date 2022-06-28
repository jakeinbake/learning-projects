import random as ran
# This is a random number guessing game.
# Things I'd like to add: More input validation, way to restart the game and update the random number
# Generate a random number right away, we'll need to move this inside of the loop somehow to allow for 'restarting' and getting a new number to guess. 
random_number = ran.randint(1,10)
# Start guess as false to force into loop
user_guess_correct = False
# Define variable used later. 
user_guess = None
# Initialize the game as 'on', we'll use this to keep the game 'live' 
game_live = True
while game_live == True:
    should_play = input("Hello, would you like to play a guessing game? Y/N ").lower()
    if should_play == ('y' or 'yes'):
        while user_guess_correct != True:
            print("Wonderful! We're playing a number guessing game!\nI've just picked out a random number between 1 & 10, go ahead and guess what it is!")
            #print(random_number) -  used in testing
            
            while user_guess != random_number:
                user_guess = int(input("Place your guess here: "))
                if user_guess == random_number:
                    user_guess_correct = True
                    print("No way! You guessed it!\nThe number was: " + str(random_number))
                    print("Thanks for playing, I'll close the game now.")
                    game_live = False
                else:
                    print("Aww, that wasn't correct. Try again!")
    elif should_play == ('n' or 'no'):
        print("Okay, maybe next time!") 
        game_live = False
    else:
        print("I don't understand, can you repeat your answer? Please respond with yes or no.")