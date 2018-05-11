#!/bin/python3

import os
import sys


def gradingStudents(grades):
    final_grades = []
    for grade in grades:
        diff = 5 - (grade % 5)
        if diff < 3:
            rounded_grade = grade + diff
            if rounded_grade < 40:
                rounded_grade = grade

            final_grades.append(rounded_grade)
        else:
            final_grades.append(grade)

    return final_grades


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
