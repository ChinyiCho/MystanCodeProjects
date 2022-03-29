"""
File: hangman.py
Name:卓晉逸
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    we get 7 chances to guess the random character
    if success, the chances will not decrease
    if run out of 7 chances, game over
    """
    life = N_TURNS                          # the chances
    ch = random_word()                      # get a random character from the function
    dashed = first_dashed(ch)               # restore the initial number of word
    print('You have ' + str(life) + ' guesses left.')
    while life > 0:                         # while loop until run out of chances
        guess = input('Your guess: ')
        if guess.isalpha() and len(guess) == 1:     # could only enter one letter
            guess = guess.upper()           # case-insensitive
            life = life_check(guess, ch, dashed, life)      # chances remain calculation
            dashed = filled(guess, ch, dashed)      # get new dashed
            if dashed == ch:                # complete the challenge
                break
            if life > 0:                    # hint for word and life
                print('The word looks like: ' + dashed)
                print('You have ' + str(life) + ' guessed left.')
            hangman(life)                   # 這行是我多加的，比較像hangman的遊戲^_^
        else:       # enter more than one letters or no english
            print('illegal format.')

    if life > 0:                            # complete the challenge
        winner()                            # 這行也是多加的
        print('You win!!')
    else:                                   # life == 0 and lose
        print('You are completely hung : (')
    print('The word was: ' + ch)


def life_check(g, ch, dashed, life):
    """
    this function check if the life should be minus
    """
    ans = ''
    for i in range(len(ch)):        # for loop for letter number of random word times
        if g == dashed[i]:          # enter the letter which has guessed before
            return life             # return the same life
        elif g == ch[i]:            # guess the letter of character
            ans += g                # input the letter to ans (dashed in main function)
        else:                       # guess not match the letter
            ans += dashed[i]        # input the old dashed
    if ans == dashed:               # ans is not changed, means that guess wrong letter
        life -= 1
    return life


def filled(g, ch, dashed):
    """
    the function check if guess matches to answer, and refresh dashed
    """
    ans = ''
    for i in range(len(ch)):        # for loop for letter number of random word times
        if g == dashed[i]:          # enter the letter which has guessed before
            print('You are correct!')
            return dashed           # return the same dashed
        elif g == ch[i]:            # guess the letter of character
            ans += g                # input the letter to ans (dashed in main function)
        else:                       # guess not match the letter
            ans += dashed[i]        # input the old dashed
    if ans == dashed:               # ans is not changed, means that guess wrong letter
        print('There is no ' + g + '\'s in the word.')
    else:                           # guess the right letter
        print('You are correct!')
    return ans


def first_dashed(ch):
    """
    initial status of dash, which tell us the letter number of random character with '-'
    """
    print('The word looks like: ', end='')
    ans = ''
    for i in range(len(ch)):        # or loop for letter number of random word times
        print('-', end='')
        ans += '-'
    print('')
    return ans


def hangman(life):
    """
    這行是我多加的，比較像hangman的遊戲^_^
    this function have no meaning for this code
    but it is fun to the player!!
    """
    if life == 7:
        print('------|--')
        print('|     |')
        print('|     O')
        print('|\n|\n|\n|\n|\n')
    elif life == 6:
        print('------|--')
        print('|     |')
        print('|     ()')
        print('|\n|\n|\n|\n|\n')
    elif life == 5:
        print('------|--')
        print('|     |')
        print('|     ()')
        print('|     |')
        print('|     |')
        print('|\n|\n|\n')
    elif life == 4:
        print('------|--')
        print('|     |')
        print('|     ()')
        print('|     |\\')
        print('|     |')
        print('|\n|\n|\n')
    elif life == 3:
        print('------|--')
        print('|     |')
        print('|     ()')
        print('|    /|\\')
        print('|     |')
        print('|\n|\n|\n')
    elif life == 2:
        print('------|--')
        print('|     |')
        print('|     ()')
        print('|    /|\\')
        print('|     |')
        print('|    /')
        print('|\n|\n')
    elif life == 1:
        print('------|--')
        print('|     |')
        print('|     ()')
        print('|    /|\\')
        print('|     |')
        print('|    / \\')
        print('|\n|\n')
    elif life == 0:
        print('------|--')
        print('|     |')
        print('|     (X)')
        print('|    /|\\')
        print('|     |')
        print('|    / \\')
        print('|\n|\n')


def winner():
    """
    WINNER
    """
    print('      ')
    print('      (_)')
    print('      \\|/')
    print('✿✿✿   |')
    print(' \\|/  / \\')



def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
