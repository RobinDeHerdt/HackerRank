#!/bin/python3

import os
import sys


def hurdleRace(init_height, hurdles):
    diff = max(hurdles) - init_height
    if diff <= 0:
        return 0

    return diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = []

    height_item = input().split()
    for i in height_item:
        height.append(int(i))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
