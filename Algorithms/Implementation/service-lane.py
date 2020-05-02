# https://www.hackerrank.com/challenges/service-lane/problem
from Testing import assertions


def serviceLane(widths, cases):

    result = []
    for case in cases:
        entry_point = case[0]
        exit_point = case[1]

        segment = widths[entry_point:exit_point+1]
        result.append(min(segment))

    return result


assertions.assert_equals([1, 2, 3, 2, 1], serviceLane([2, 3, 1, 2, 3, 2, 3, 3], [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]))
assertions.assert_equals([2, 1, 1, 1, 2], serviceLane([1, 2, 2, 2, 1], [[2, 3], [1, 4], [2, 4], [2, 4], [2, 3]]))
