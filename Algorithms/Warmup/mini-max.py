#!/bin/python3

import os
import sys


def miniMaxSum(arr):
    arr.sort()

    min_result = 0
    for i in arr[:len(arr) - 1]:
        min_result += i

    max_result = 0
    for i in arr[1:]:
        max_result += i

    print(min_result, max_result)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
