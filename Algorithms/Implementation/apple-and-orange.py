#!/bin/python3

import os
import sys


def countFruits(house_left_bound, house_right_bound, tree_pos, fruits):
    hit_count = 0
    for fruit in fruits:
        fall_pos = tree_pos + fruit
        if fall_pos >= house_left_bound and fall_pos <= house_right_bound:
            hit_count += 1

    print(hit_count)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    countFruits(s, t, a, apple)
    countFruits(s, t, b, orange)
