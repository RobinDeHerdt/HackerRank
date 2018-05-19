#!/bin/python3

import os


def designerPdfViewer(ar, word):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    tallest_value = 0
    for char in word:
        index = alphabet.index(char)
        if ar[index] > tallest_value:
            tallest_value = ar[index]

    return tallest_value * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(ar, word)

    fptr.write(str(result) + '\n')

    fptr.close()
