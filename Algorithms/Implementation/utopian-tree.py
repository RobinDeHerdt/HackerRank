#!/bin/python3

import os


def utopianTree(n):
    height = 1
    for i in range(n):
        if i % 2 == 0:
            # Spring condition
            height *= 2
        else:
            # Summer condition
            height += 1

    return height


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
