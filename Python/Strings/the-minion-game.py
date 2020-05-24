# https://www.hackerrank.com/challenges/the-minion-game/problem
from Testing import assertions
from collections import Counter

# Since 0 < len(string) <= 10^6, provide an alternative approach.
def minion_game(string):

    vowels = ['A', 'E', 'I', 'O', 'U']
    string_length = len(string)

    starting_with_vowel = 0
    starting_with_consonant = 0

    for i in range(string_length):
        if string[i] in vowels:
            starting_with_vowel += string_length - i
        else:
            starting_with_consonant += string_length - i

    if starting_with_vowel > starting_with_consonant:
        return 'Kevin {0}'.format(starting_with_vowel)
    elif starting_with_vowel < starting_with_consonant:
        return 'Stuart {0}'.format(starting_with_consonant)
    else:
        return 'Draw'

def minion_game_bruteforce(string):

    vowels = ['A', 'E', 'I', 'O', 'U']

    starting_with_vowel = []
    starting_with_consonant = []

    string_length = len(string)
    for i in range(string_length + 1):
        for j in range(string_length + 1):
            substr = string[i:j]
            if not substr:
                continue

            if substr[0] in vowels:
                starting_with_vowel.append(substr)
            else:
                starting_with_consonant.append(substr)

    # This will give an overview of substring occurrences.
    # print(Counter(starting_with_vowel))
    # print(Counter(starting_with_consonant))

    if len(starting_with_vowel) > len(starting_with_consonant):
        return 'Kevin {0}'.format(len(starting_with_vowel))
    elif len(starting_with_vowel) < len(starting_with_consonant):
        return 'Stuart {0}'.format(len(starting_with_consonant))
    else:
        return 'Draw'

assertions.assert_equals('Stuart 12', minion_game_bruteforce('BANANA'))
assertions.assert_equals('Stuart 12', minion_game('BANANA'))