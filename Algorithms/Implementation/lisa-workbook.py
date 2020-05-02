# https://www.hackerrank.com/challenges/lisa-workbook/problem
from Testing import assertions


def workbook(n, k, arr):
    special_problems = 0
    current_page = 1
    for chapter in createWorkBook(arr, k):
        for page in chapter:
            for problem in page:
                if problem == current_page:
                    special_problems += 1

            current_page += 1

    return special_problems


# Create a multidimensional array representation of a 'workbook'
def createWorkBook(arr, problems_per_page):
    chapters = []
    for problem_count in arr:
        problems = list(range(1, problem_count + 1))
        chapters.append(chunk(problems, problems_per_page))

    return chapters


# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
def chunk(arr, chunk_size):
    return [arr[i * chunk_size:(i + 1) * chunk_size] for i in range((len(arr) + chunk_size - 1) // chunk_size )]


assertions.assert_equals(4, workbook(5, 3, [4, 2, 6, 1, 10]))
assertions.assert_equals(8, workbook(10, 5, [3, 8, 15, 11, 14, 1, 9, 2, 24, 31]))
