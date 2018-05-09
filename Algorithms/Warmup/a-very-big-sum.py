#!/bin/python3

import os
import sys


def aVeryBigSum(n, ar):
    result = 0
    for i in ar:
        result += i

    return result


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(n, ar)

    f.write(str(result) + '\n')

    f.close()
