#!/bin/python3

import math
import os
import random
import re
import sys


def encryption(s):
    def slice(s, n):
        for start in range(0, len(s), n):
            yield s[start:start + n]

    s = s.replace(" ", "")
    length = len(s)

    row_count = math.floor(math.sqrt(length))
    column_count = math.ceil(math.sqrt(length))

    grid = []
    for slice in slice(s, column_count):
        grid.append(list(slice))

    encrypted_string = ""
    for i in range(column_count):
        for row in grid:
            if len(row) <= i:
                continue

            encrypted_string += row[i]

        encrypted_string += " "

    return encrypted_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
