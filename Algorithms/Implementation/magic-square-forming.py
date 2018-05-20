#!/bin/python3

import os
import copy


def formingMagicSquare(matrix):
    def getHorizontalSums(matrix):
        horizontal_sums = []
        for line in matrix:
            horizontal_sums.append(sum(line))

        return horizontal_sums

    def getVerticalSums(matrix):
        vertical_sums = []
        for i in range(3):
            line_sum = 0
            for line in matrix:
                line_sum += line[i]

            vertical_sums.append(line_sum)

        return vertical_sums

    def getDiagonalSums(matrix):
        diagonal_sums = []

        index = 0
        line_sum = 0
        for line in matrix:
            line_sum += line[index]
            index += 1

        diagonal_sums.append(line_sum)

        index = 2
        line_sum = 0
        for line in matrix:
            line_sum += line[index]
            index -= 1

        diagonal_sums.append(line_sum)

        return diagonal_sums

    def getMissingNumbers(matrix):
        numbers = list(range(1, 10))
        for line in matrix:
            for value in line:
                if value in numbers:
                    numbers.remove(value)

        return numbers

    def getDuplicateNumbers(matrix):
        numbers = []
        duplicates = []
        for line in matrix:
            for value in line:
                if value in numbers:
                    duplicates.append(value)
                    continue

                numbers.append(value)

        return duplicates

    def isValidMatrix(matrix):
        horizontal_sums = getHorizontalSums(matrix)
        vertical_sums = getVerticalSums(matrix)
        diagonal_sums = getDiagonalSums(matrix)

        sums = horizontal_sums + vertical_sums + diagonal_sums

        # Set the first value as the default magic constant
        magic_constant = sums[0]
        for i in sums:
            if i != magic_constant:
                return False

        return True

    duplicates = getDuplicateNumbers(matrix)
    missing_numbers = getMissingNumbers(matrix)
    for line_index, line in enumerate(matrix):
        for index, value in enumerate(line):
            if value in duplicates:
                for i in missing_numbers:
                    original_matrix = copy.deepcopy(matrix)
                    matrix[line_index][index] = i
                    print(matrix)
                    if isValidMatrix(matrix):
                        return i - value
                    else:
                        matrix = copy.deepcopy(original_matrix)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
