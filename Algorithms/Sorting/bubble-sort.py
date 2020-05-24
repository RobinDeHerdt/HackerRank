# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
from Testing import assertions

def bubble_sort(arr):

    arr_len = len(arr)
    swap_count = 0

    for i in range(arr_len):
        for j in range(arr_len - 1):
            current_element = arr[j]
            if current_element > arr[j+1]:
                arr[j] = arr[j+1]
                arr[j+1] = current_element
                swap_count += 1

    # Required test output on hackerrank.
    # print("Array is sorted in {0} swaps.".format(swap_count))
    # print("First Element: {0}".format(arr[0]))
    # print("Last Element: {0}".format(arr[-1]))

    return arr


assertions.assert_equals([1, 2, 3], bubble_sort([3, 2, 1]))
assertions.assert_equals([1, 2, 3, 4], bubble_sort([4, 2, 3, 1]))

