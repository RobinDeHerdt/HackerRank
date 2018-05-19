#!/bin/python3

import os


def permutationEquation(arr):
    results = []
    for index, value in enumerate(arr, start=1):
        found_index = arr.index(index) + 1
        results.append(arr.index(found_index) + 1)

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
