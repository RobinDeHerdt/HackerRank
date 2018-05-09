#!/bin/python3

import os
import sys


def diagonalDifference(matrix):
    d1 = 0
    for index, region in enumerate(matrix):
        for number_index, number in enumerate(region):
            if number_index == index:
                d1 += number

    matrix.reverse()

    d2 = 0
    for index, region in enumerate(matrix):
        for number_index, number in enumerate(region):
            if number_index == index:
                d2 += number

    return abs(d1 - d2)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
