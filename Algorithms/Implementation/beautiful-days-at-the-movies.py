#!/bin/python3

import os


def beautifulDays(i, j, k):
    total_amount = 0
    for date in range(i, j):
        reversed_date = str(date)
        reversed_date = int(reversed_date[::-1])

        if (date - reversed_date) % k == 0:
            # Date is considered beautiful
            total_amount += 1

    return total_amount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
