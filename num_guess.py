#!/usr/bin/env python3

# Created by Billy Terimpundu
# Created on December 2021
# This program gets the user to guess a number
# between 0 and 9 and tells them if it's correct.
import constants

def main():

    # input
    guess_number = float(input("Guess a number between 0 and 9: "))
    print("")

    # Process and output
    if guess_number == constants.CORRECT_GUESS:
        print ("you guessed it right!")

    else:
        print ("you guessed it wrong!") 


if __name__ == "__main__":
    main()
