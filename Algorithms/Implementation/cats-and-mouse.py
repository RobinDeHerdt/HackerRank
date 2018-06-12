#!/bin/python3

import os


def catAndMouse(x, y, z):
    diff_a = abs(x - z)
    diff_b = abs(y - z)

    if diff_a == diff_b:
        return "Mouse C"
    elif diff_a > diff_b:
        return "Cat B"
    else:
        return "Cat A"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
