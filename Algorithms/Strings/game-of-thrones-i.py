#!/bin/python3

import sys


def gameOfThrones(s):
    char_counts = []
    processed_characters = []
    for char in s:
        if char in processed_characters:
            continue

        char_counts.append(s.count(char))
        processed_characters.append(char)

    center_var = False
    for i in char_counts:
        if i % 2 != 0:
            if center_var:
                return "NO"

            center_var = True

    return "YES"


s = input().strip()
result = gameOfThrones(s)
print(result)
