#!/bin/python3

from collections import deque
import os


def circularArrayRotation(arr, rotation_count, indexes):
    items = deque(arr)
    items.rotate(rotation_count)

    results = []
    for i in indexes:
        results.append(items[i])

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    m = []

    for _ in range(q):
        m_item = int(input())
        m.append(m_item)

    result = circularArrayRotation(a, k, m)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
