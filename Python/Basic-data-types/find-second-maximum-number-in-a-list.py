# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

from Testing import assertions


def find_second_maximum_number_in_list(arr):
    # Convert the map to a set; only unique values will remain.
    unique_arr_values = set(arr)

    # Convert the set to a list, so we can sort it.
    unique_arr_values = list(unique_arr_values)
    unique_arr_values.sort()

    return unique_arr_values[-2]


assertions.assert_equals(5, find_second_maximum_number_in_list([2, 3, 6, 6, 5]))
assertions.assert_equals(4, find_second_maximum_number_in_list([7, 0, 4, 2, 3]))
