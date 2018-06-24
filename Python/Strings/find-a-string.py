#!/bin/python3


def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        substr_length = len(sub_string)
        if(string[i:i+substr_length] == sub_string):
            count += 1

    return count
