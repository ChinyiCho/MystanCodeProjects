"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
from typing import List

FILE = 'dictionary.txt'


def main():
    """
    TODO:
    """
    letters: List[str] = []
    for i in range(4):
        print(i + 1, end=' ')
        s: str = input('row of letters: ')
        l: List[str] = s.split(' ')
        for c in l:
            if len(c) != 1:
                print('Illegal input')
                break
        letters.append(l)
    # print(letters)
    # letters = [['c', 'e', 'n', 'i'], ['h', 'h', 'r', 'y'], ['u', 'n', 'e', 'j'], ['n', 't', 'a', 'e']]
    start = time.time()
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    dic = read_dictionary()
    fin = []
    for i in range(len(letters)):
        for j in range(len(letters[i])):
            find_boggle(j, i, letters, '', dic, fin, [])
    print('There are', len(fin), 'words in total')
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_boggle(x, y, letters, cur, dic, fin, before_index):
    cur += letters[y][x]
    all_choices = []

    if has_prefix(cur, dic):
        if len(cur) >= 4:
            if cur in dic:
                if cur not in fin:
                    print('Found', cur)
                    fin.append(cur)
                    # print(fin)
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                blin = True
                if 0 <= x + i < 4 and 0 <= y + j < 4:
                    if i != 0 or j != 0:
                        for b in range(len(before_index)):
                            if x + i == before_index[b][0] and y + j == before_index[b][1]:
                                blin = False
                        if blin:
                            all_choices.append([x + i, y + j])
        for choice in all_choices:
            before_index.append([x, y])
            find_boggle(choice[0], choice[1], letters, cur, dic, fin, before_index)
            # cur = cur[:len(cur) - 1]
            before_index.pop()
            # print(before_index)


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        d = []
        for line in f:
            line = line.split('\n')[0]
            d.append(line)
    return d


def has_prefix(sub_s, dic):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for d in dic:
        if d.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
