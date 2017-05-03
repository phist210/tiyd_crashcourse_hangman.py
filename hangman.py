'''
https://tinyurl.com/hangmanpythontiyd
https://repl.it/HbxI/2

Welcome! Today we will implement the classic game, Hangman!

We will talk about:
    1. What Python is and where it came from
    2. Who uses Python
    3. Objects
        - Variables (named buckets that hold data)

        - Data types

            > Strings (characters "string'ed" together to represent text)
            > Integers (plain ol' whole numbers)
            > Operators (math stuff: + - > >= < <= /...)
            > Lists (a type of collection of objects, connected by [,])
            > Booleans (True or False)
            > we'll add more as we go

        - Functions (a set of instructions, essentially)
            > def add(x, y):   ---->    add(5, 6)
                  return x + y  ---->        11


    4. Writing the game

1. Created by Guido van Rossum and first released in 1991, Python is an interpreted programming language.
    For those who don't know, a programming language is what you write down to tell a computer what to do.
    However, the computer doesn't read the language directly - there are hundreds of programming languages, and it couldn't understand them all.
    So, when someone writes a program, they will write it in their language of choice,
    and then compile it - that is, turn it in to lots of 0s and 1s, that the computer can easily and quickly understand.

2. Big-name companies use and have been using Python for some time now:
    Google, Yahoo Maps, Red Hat, Nokia, Walt Disney, NASA, IBM...

3. Everything in Python is an object and almost everything
    has ATTRIBUTES and METHODS (things and actions objects know about themselves).

These are just a few things to give us some foundation to start writing.
'''

# Let's make a list of words and choose one as our secret_word.

# Let's get input from the player and assign it to a variable, guess.

# With guess, we'll compare it to our secret_word and keep track of guesses.

# Draw a board that shows bad guesses, strikes and spaces for our secret_word.

# To allow the flow of the game, we will use a while loop with the "done" flag.


from random import choice
import os
import time
import sys


def welcome():
    '''
    Presents user with a welcome screen
    '''
    clear()
    print('\n** Welcome to Hangman!!! **\n')
    start = input("Press ENTER to start or Q to quit: ").lower()

    if start == 'q':
        print("See you next time!")
        sys.exit()  # runs the exit() function on the command line

    return


def clear():
    '''
    This applies for Linux/Mac, use 'cls' in place of 'clear' for Windows
    '''
    os.system('clear')


def get_secret_word():
    '''
    Returns a random word from words list
    '''
    words = ['angry', 'beautiful', 'brave', 'careful', 'careless', 'clever',
             'crazy', 'cute', 'dangerous', 'exciting', 'famous', 'friendly',
             'happy', 'interesting', 'lucky', 'old', 'poor', 'popular', 'rich',
             'thin', 'young']

    return choice(words)


def get_guess(secret_word, bad_guesses, good_guesses):
    '''
    Prompts user for a guess and validates the guess before returning
    '''
    while True:
        guess = input("Guess a letter: ").lower()

        if guess == '':
            input("Sorry, didn't catch that... Hit ENTER to continue.")

        elif len(guess) != 1:
            input("You can only guess a SINGLE letter! Hit ENTER to continue.")

        elif guess in bad_guesses or guess in good_guesses:
            input("You've already guessed that letter! Hit ENTER to continue.")

        elif not guess.isalpha():
            input("You can only guess LETTERS! Hit ENTER to continue.")

        else:
            return guess


def board(bad_guesses, good_guesses, secret_word):
    '''
    Clears the terminal screen and draws a board for the game
    '''
    clear()

    print('** Strikes: {}/8 **'.format(len(bad_guesses)))
    print('')

    for guess in bad_guesses:  # displays bad guesses as a tally
        print(guess, end=" ")
    print('\n\n')

    for guess in secret_word:
        if guess in good_guesses:
            print(guess, end=" ")
        else:
            print(' _ ', end=" ")  # displays blank spaces until a good guess

    print('')


def game():
    """
    Play a single game of Hangman.  Return True if the player wins,
    or False if the player loses.
    """
    welcome()
    secret_word = get_secret_word()
    good_guesses = []
    bad_guesses = []
    done = False

    while not done:
        board(bad_guesses, good_guesses, secret_word)
        guess = get_guess(secret_word, good_guesses, bad_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            if all(letter in good_guesses for letter in secret_word):
                print("You win!")
                print("The secret word was {}.".format(secret_word))
                done = True

        elif guess not in secret_word:
            bad_guesses.append(guess)
            if len(bad_guesses) == 8:
                clear()
                print("\n **  ENGHH!  ** ")
                print("\nStrike ! You lost!")
                print("\nThe secret word was {}".format(secret_word.upper()))
                done = True

        else:
            board(bad_guesses, good_guesses, secret_word)


def play_again():
    """
    Ask the player whether to play again.
    """
    return 'n' != input("\nPlay again? Y/n ").lower()


def main():
    """
    Play games of Hangman until the user decides to quit.
    """
    while True:
        game()
        if not play_again():
            print("\n\n\n\nCatch ya later!\n\n\n\n")
            break
        clear()


main()
