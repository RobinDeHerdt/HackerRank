#!/bin/python3

import os


def viralAdvertising(n):
    likes = 2
    recipients = 5
    for day in range(1, n):
        recipients = (recipients // 2) * 3
        likes += (recipients // 2)

    return likes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
