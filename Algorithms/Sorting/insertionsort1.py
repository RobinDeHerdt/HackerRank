# https://www.hackerrank.com/challenges/insertionsort1/problem?h_r=next-challenge&h_v=zen
def insertionSort1(arr):

    value = arr[len(arr) - 1]
    for i in range(len(arr) - 1, -1, -1):
        if i == 0 or value > arr[i - 1]:
            arr[i] = value
            break

        arr[i] = arr[i - 1]
        print(' '.join(map(str, arr)))

    print(' '.join(map(str, arr)))


insertionSort1([2, 4, 6, 8, 3])
insertionSort1([2, 3, 4, 5, 6, 7, 8, 9, 10, 1])

