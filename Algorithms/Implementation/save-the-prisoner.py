#!/bin/python3

import os


def saveThePrisoner(prisoners, treats, start):
    rest = (treats + start - 1) % prisoners
    if rest == 0:
        return prisoners
    else:
        return rest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
