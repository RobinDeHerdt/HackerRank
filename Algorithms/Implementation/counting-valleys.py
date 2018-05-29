#!/bin/python3

import os


def countingValleys(n, arr):
    level = 0
    valley_count = 0
    currently_in_valley = False
    for i in arr:
        if i == 'U':
            level += 1

        if i == 'D':
            level -= 1

        if level == -1:
            currently_in_valley = True

        if level == 0 and currently_in_valley:
            valley_count += 1
            currently_in_valley = False

    return valley_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
