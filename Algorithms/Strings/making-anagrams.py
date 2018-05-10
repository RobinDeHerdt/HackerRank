#!/bin/python3

import sys


def makingAnagrams(string1, string2):
    for char in string1:
        if char in string2:
            string1 = string1.replace(char, "", 1)
            string2 = string2.replace(char, "", 1)

    return len(string1) + len(string2)


s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)
