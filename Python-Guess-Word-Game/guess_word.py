# Guess word game
# Word from bip39

import random
from bip39 import bip39_list
import string

# random word from bip39.py
def random_word():
    word = random.choice(bip39_list)

    # print for check the word
    # print(word)
    word_list = list(word)
    return word_list

# function to turn List to String for the answer
def ListToString(s):
    strl = ""
    for a in s:
        strl += a
    return strl

# game function
def game_start():
    guess_word = random_word()
    my_ans_list = list()
    used_letters = list()

    # create your blank answer
    for i in guess_word:
        my_ans_list.append('_')

    while my_ans_list != guess_word:
        # print your answer
        print(f"My answer : {my_ans_list}")

        # getting user input
        user_input = input("Type a charecter : ").lower()

        # check user's charecter input has not been used
        if user_input not in used_letters:
            # check user's charecter in the answer
            if user_input in guess_word:
                # if yes : check the answer index
                for j in range(len(guess_word)):
                    if user_input == guess_word[j]:
                        my_ans_list[j] = user_input
            # if not
            else :
                print("Your charecter is not correct \nTry Again!!")
            # Add used charecter
            used_letters.append(user_input)
        else:
            print("You have used that charecter. \nPlease try again")
        print(f"Used letter : {used_letters}")
    print(f"My answer is {my_ans_list}")
    print(f"The answer word is {ListToString(guess_word)}")

game_start()