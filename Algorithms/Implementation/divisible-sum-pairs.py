#!/bin/python3

import math
import os
import random
import re
import sys


def divisibleSumPairs(k, numbers):
    result_count = 0
    for index, value in enumerate(numbers):
        for j_index, j_value in enumerate(numbers):
            if index <= j_index:
                continue

            if (value + j_value) % k == 0:
                result_count += 1

    return result_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
