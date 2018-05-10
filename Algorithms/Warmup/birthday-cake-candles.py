#!/bin/python3

import os
import sys


def birthdayCakeCandles(ar):
    max = 0
    for i in ar:
        if i > max:
            max = i

    return ar.count(max)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    f.write(str(result) + '\n')

    f.close()
