#!/bin/python3


def mutate_string(string, position, character):
    arr = list(string)
    arr[position] = character
    return ''.join(arr)