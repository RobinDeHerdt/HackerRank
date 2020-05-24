# https://www.hackerrank.com/challenges/array-left-rotation/problem
from Testing import assertions


def left_rotate(rotations, arr):
    if rotations == len(arr):
        return arr

    if rotations > len(arr):
        rotations = rotations % len(arr)

    return arr[rotations:] + arr[:rotations]


assertions.assert_equals([5, 1, 2, 3, 4], left_rotate(4, [1, 2, 3, 4, 5]))
assertions.assert_equals([1, 2, 3, 4, 5], left_rotate(5, [1, 2, 3, 4, 5]))
assertions.assert_equals([1, 2, 3, 4, 5], left_rotate(10, [1, 2, 3, 4, 5]))
assertions.assert_equals([5, 1, 2, 3, 4], left_rotate(14, [1, 2, 3, 4, 5]))