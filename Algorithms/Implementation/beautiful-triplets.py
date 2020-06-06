# https://www.hackerrank.com/challenges/beautiful-triplets/problem
from Testing import assertions

def beautiful_triplets(d, arr):

    result_count = 0

    arr_len = len(arr)
    for i in range(arr_len):
        if i >= arr_len - 1:
            continue

        current = arr[i]

        one_step_ahead = current + d
        two_steps_ahead = current + d + d

        if one_step_ahead in arr and two_steps_ahead in arr:
            result_count += 1

    return result_count

assertions.assert_equals(3, beautiful_triplets(3, [1, 2, 4, 5, 7, 8, 10]))
assertions.assert_equals(2, beautiful_triplets(3, [1, 6, 7, 7, 8, 10, 12, 13, 14, 19]))

