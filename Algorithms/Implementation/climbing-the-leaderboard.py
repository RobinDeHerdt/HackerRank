#!/bin/python3

import os
import sys


def climbingLeaderboard(leaderboard_scores, personal_scores):
    leaderboard = list(sorted(set(leaderboard_scores)))
    leaderboard.reverse()

    results = []
    for personal_score in personal_scores:

        low_bound = 0
        high_bound = len(leaderboard)
        while low_bound < high_bound:
            middle = (low_bound + high_bound) // 2

            if personal_score > leaderboard[middle]:
                high_bound = middle
            else:
                low_bound = middle + 1

        prev_index = low_bound - 1
        if prev_index >= 0 and leaderboard[prev_index] == personal_score:
            results.append(low_bound)
        else:
            leaderboard.insert(low_bound, personal_score)
            results.append(low_bound + 1)

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
