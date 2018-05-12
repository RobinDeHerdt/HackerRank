#!/bin/python3

import os
import sys


def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]

    broken_max_record_count = 0
    broken_min_record_count = 0

    for score in scores:
        if score > max_score:
            max_score = score
            broken_max_record_count += 1

        if score < min_score:
            min_score = score
            broken_min_record_count += 1

    return broken_max_record_count, broken_min_record_count


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
