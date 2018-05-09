#!/bin/python3

import os
import sys


def solve(a, b):
    a_points, b_points = 0, 0
    for i in range(0, 3):
        if int(a[i]) > int(b[i]):
            a_points += 1

        if int(a[i]) < int(b[i]):
            b_points += 1

    return a_points, b_points


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a0A1A2 = input().split()
    b0B1B2 = input().split()

    result = solve(a0A1A2, b0B1B2)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
