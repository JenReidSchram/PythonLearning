#!/usr/bin/env python3

import random
import sys

# Set up some global variables. TODO: Add ability to play multiple games and move this into the Main function
with open('hangmanwords.txt', mode='rt', encoding='utf-8') as w:
    word_list = [line.strip() for line in w]

play_word = word_list[random.randint(0, len(word_list) - 1)]
puzzle = ['- '] * len(play_word)
letters_played = []


def validate_input(a):
    """
    Validates the input from the user, checking if it's empty, multiple letters or a non-alphnumeric value
    :param a: letter input
    :return: invalid flag
    """
    invalid = 0
    if len(a) != 1:
        invalid = 1
        print("You must enter a single letter")
    elif not a.isalpha():
        invalid = 1
        print("You must enter a letter")
    return invalid


def check_for_match(l):
    """
    Checks whether the inputted letter matches against the play_word and, if so, how many times it is in the word
    :param l: letter input
    :return: match flag
    """
    match = 0
    # TODO: Track if a letter has already been played and return a message to the user (don't decrement bad guess)
    # if l in letters_played:
    #     print("You've already played {}".format(l.upper()))

    if l in play_word:
        match = 1
        x = play_word.count(l)
        print("You got a letter! {0} appears {1} times".format(l.upper(), x))
        print(' '.join(remaining_puzzle(l, x)).upper())
    else:
        print("Nope. {0} does not appear in the word".format(l.upper()))
    return match


def remaining_puzzle(p, count):
    """
    Calculates the remaining puzzle visual (- - - -) by incrementally slicing the play_word and checking for matches
    :param p: letter input
    :param count: number of times letter appears in word (from check_for_match)
    :return: newly-calculated puzzle visual
    """
    ind_start = 0
    ind_end = len(puzzle)+1
    for i in range(count):
        '''We want to find every instance of the letter in the word
           For each iteration, we update the initial index for the slice 
           and only look at those letters after the previous instance'''
        pos = play_word[ind_start:ind_end].index(p)
        puzzle[pos + ind_start] = p
        ind_start += pos + 1
    return puzzle


def main(test=0, bad_guesses=5):
    num_bad_guesses = bad_guesses

    if test:
        print(play_word)

    print("Your word has {0} letters".format(len(play_word)))
    print(''.join(puzzle))
    print("You have {0} bad guesses remaining".format(num_bad_guesses))

    while num_bad_guesses:
        guess = input("Guess a letter: ")
        c = validate_input(guess)
        if not c:
            b = check_for_match(guess)
            if '- ' not in puzzle:  # Player has guessed all letters
                break
            if not b:
                num_bad_guesses -= 1
                print("You have {0} bad guesses remaining".format(num_bad_guesses))

    if num_bad_guesses:
        print("Congratulations! You guessed the word: {0}".format(play_word.upper()))
    else:
        print("Better luck next time! Your word was {0}".format(play_word.upper()))


if __name__ == '__main__':
    main(test=int(sys.argv[1]),
         bad_guesses=int(sys.argv[2]))







