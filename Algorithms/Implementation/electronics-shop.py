#!/bin/python3

import os
import sys


def getMoneySpent(keyboards, drives, b):
    diffs = []
    for keyboard in keyboards:
        for drive in drives:
            diff = b - (keyboard + drive)
            if diff >= 0:
                diffs.append(diff)

    if len(diffs) == 0:
        return -1

    return b - min(diffs)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
