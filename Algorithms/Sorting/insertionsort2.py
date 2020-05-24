# https://www.hackerrank.com/challenges/insertionsort2/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def insertionSort2(arr):

    value = arr[len(arr) - 1]
    for i in range(len(arr) - 1, -1, -1):
        if i == 0 or value > arr[i - 1]:
            arr[i] = value
            break

        arr[i] = arr[i - 1]
        print(' '.join(map(str, arr)))

    print(' '.join(map(str, arr)))


insertionSort2([1, 4, 3, 5, 6, 2])

