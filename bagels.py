"""
Deductive logic game that gives cluses so user can guess a three digit number
"""

#initialize variables
num_digits = 3
max_guesses = 10

def main():
    print('''Bagels, a deductive logic game.
          I'm thinking of a {}-digit number with no repeated digits.
          Try to guess what it is. Here are some clues:
          When I say:   That means:
            Pico        One digit is correct but in the wrong position.
            Fermi       One digit is correect and in the right position.
            Bagels      No digit is correct.
          
          For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.'''.format(num_digits))
    
    #This loop is the main loop for the game
    while True:

        #the variable secretNum is what stores the secret number the player needs to get. It is initialized with the getSecretNum function
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(max_guesses))

        numGuesses = 1
        while numGuesses <= max_guesses:
            guess = ''
            # This will keep the programming looping until a valid guess is entered
            # note that len = length, so it clunts the amount of guesses in the guess variable
            while len(guess) != num_digits or not guess.isdecimal(): #while the length of the guesses is not equal to the number of digits or it is not a decimal
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ') #asks the user for an input, which is stored in the guess variable
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess ==  secretNum:
                break #we break out of the loop if the guess is right/matches the secretNumber
            if numGuesses > max_guesses:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))
        
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing!')

def getSecretNum():
    print()
