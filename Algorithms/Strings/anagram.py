#!/bin/python3

import sys


def anagram(s):
    str_length = len(s)
    if str_length % 2 != 0:
        return -1

    substr_length = str_length // 2

    substr1 = s[substr_length:]
    substr2 = s[:substr_length]

    changes = 0
    processed_chars = []
    for char in substr1:
        if char in processed_chars:
            continue

        changes += max(0, (substr1.count(char) - substr2.count(char)))
        processed_chars.append(char)

    return changes


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)
