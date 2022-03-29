"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
from typing import List

FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        s: str = input('Find anagrams for: ')
        if s == EXIT:
            break
        else:
            start = time.time()
            print('Searching...')
            ####################
            #                  #
            #       TODO:      #
            #                  #
            ####################
            dic: List[str] = read_dictionary()
            s_lst: List[str] = find_anagrams(s=s)
            total_lst: List[str] = []
            for s_anagram in s_lst:
                if search(s_anagram, dic, '', 0):
                    if s_anagram in dic:
                        print('Found: ', s_anagram)
                        print('Searching...')
                        total_lst.append(s_anagram)
            print(len(total_lst), 'anagrams: ', total_lst)
            end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def search(s_anagram, dic, sub_s, i):
    if len(sub_s) > 0 and not has_prefix(sub_s, dic):
        return False
    if len(sub_s) == i:
        return True
    return search(s_anagram, dic, sub_s + s_anagram[i], i + 1)


def read_dictionary():
    with open(FILE, 'r') as f:
        d = []
        for line in f:
            line = line.split('\n')[0]
            d.append(line)
    return d


def find_anagrams(s: str):
    current_s =''
    length = len(s)
    s_lst = []
    find_anagrams_new(s, current_s, length, s_lst)
    return s_lst


def find_anagrams_new(s, current_s, length, s_lst):
    """
    :param s:
    :return:
    """
    new = ''
    if len(current_s) == length:
        if current_s not in s_lst:
            s_lst.append(current_s)
    else:
        for i in range(len(s)):
            new = s[:i] + s[i+1:]
            find_anagrams_new(new, current_s + s[i], length, s_lst)


def has_prefix(sub_s, dic):
    """
    :param sub_s:
    :return:
    """
    for d in dic:
        if d.startswith(sub_s):
            return True
    return False

if __name__ == '__main__':
    main()
