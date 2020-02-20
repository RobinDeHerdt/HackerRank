if __name__ == '__main__':
    arr = [2, 3, 6, 6, 5]

    # Convert the map to a set; only unique values will remain.
    unique_arr_values = set(arr)

    # Convert the set to a list, so we can sort it.
    unique_arr_values = list(unique_arr_values)
    unique_arr_values.sort()

    print(unique_arr_values[-2])