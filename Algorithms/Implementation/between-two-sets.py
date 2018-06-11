#!/bin/python3

import os
import sys


def getTotalX(a, b):
    results = 0
    for x in range(max(a), min(b) + 1):
        divideA = [x % j != 0 for j in a]
        divideB = [j % x != 0 for j in b]

        if sum(divideA) == 0 and sum(divideB) == 0:
            results += 1

    return results


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
