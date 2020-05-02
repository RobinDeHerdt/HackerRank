# https://www.hackerrank.com/challenges/equality-in-a-array/problem
from collections import Counter
from Testing import assertions


def equalizeArray(arr):
    # Count occurrences of every unique item in the given array.
    arr_value_counts = Counter(arr)

    # Sort the dictionary based on value.
    arr_value_counts = {k: v for k, v in sorted(arr_value_counts.items(), key=lambda item: item[1])}

    equalizer_value = list(arr_value_counts.keys())[-1]
    equalizer_value_occurrences = arr_value_counts[equalizer_value]

    return len(arr) - equalizer_value_occurrences


assertions.assert_equals(2, equalizeArray([1, 21, 21, 3]))
assertions.assert_equals(3, equalizeArray([3, 3, 2, 1, 3, 1]))
assertions.assert_equals(4, equalizeArray ([3, 3, 2, 1, 3, 1, 0]))


