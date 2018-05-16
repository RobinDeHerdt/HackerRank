#!/bin/python3

import os
import sys


def migratoryBirds(n, birds):
    bird_dictionary = {}

    for bird in birds:
        if bird in bird_dictionary:
            bird_dictionary[bird] = bird_dictionary.get(bird) + 1
        else:
            bird_dictionary[bird] = 1

    return max(bird_dictionary, key=bird_dictionary.get)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = migratoryBirds(ar_count, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
