#!/bin/python3

import os


def bonAppetit(k, bill, charged_amount):
    bill.pop(k)

    bill_total = 0
    for i in bill:
        bill_total += i

    bill_half = int(bill_total / 2)
    if bill_half == charged_amount:
        return "Bon Appetit"
    else:
        return charged_amount - bill_half


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    m = int(input())

    result = bonAppetit(k, ar, m)

    fptr.write(str(result) + '\n')

    fptr.close()
