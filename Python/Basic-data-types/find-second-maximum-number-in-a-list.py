# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':

    def find_second_maximum_number_in_list(arr):
        # Convert the map to a set; only unique values will remain.
        unique_arr_values = set(arr)

        # Convert the set to a list, so we can sort it.
        unique_arr_values = list(unique_arr_values)
        unique_arr_values.sort()

        return unique_arr_values[-2]

    def assert_equals(expected, actual):
        assert expected == actual, "Expected {0} but got {1}".format(expected, actual)
        print("\033[92m [SUCCESS] {0} equals {1}".format(expected, actual))

    assert_equals(5, find_second_maximum_number_in_list([2, 3, 6, 6, 5]))
    assert_equals(4, find_second_maximum_number_in_list([7, 0, 4, 2, 3]))
