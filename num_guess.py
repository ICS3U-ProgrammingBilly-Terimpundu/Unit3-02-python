#!/usr/bin/env python3

# Created by Billy Terimpundu
# Created on December 2021
# This program ask user to guess a number
# between 0 and 9 and tells the user if it's correct.
import constants

def main():

    # input
    guess_number = float(input("Guess a number between 0 and 9: "))
    print("")

    # Process and output
    if guess_number == constants.CORRECT_GUESS:
        print ("well done,You guessed it right!")

    else:
        print ("Sorry You guessed it wrong,try again next time!")


if __name__ == "__main__":
    main()
    