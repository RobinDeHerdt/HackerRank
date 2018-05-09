#!/bin/python3

import os
import sys


def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0

    length = len(arr)
    for i in arr:
        if i < 0:
            neg += 1
        elif i > 0:
            pos += 1
        else:
            zer += 1

    print("{:.6f}".format(pos / length))
    print("{:.6f}".format(neg / length))
    print("{:.6f}".format(zer / length))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
