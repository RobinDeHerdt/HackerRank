#!/bin/python3

import os


def angryProfessor(k, times):
    amount_of_students = len(times)
    max_latecomers = amount_of_students - k
    print(max_latecomers)
    latecomers = 0
    for time in times:
        if time > 0:
            # Considered late
            latecomers += 1

        if latecomers > max_latecomers:
            return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        ar = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, ar)

        fptr.write(result + '\n')

    fptr.close()
