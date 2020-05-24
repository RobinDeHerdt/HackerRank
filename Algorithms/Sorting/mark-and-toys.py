# https://www.hackerrank.com/challenges/mark-and-toys/problem
from Testing import assertions

def maximumToys(prices, k):
    prices.sort()

    i = 0
    total = 0
    while True:
        total += prices[i]
        if total >= k:
            return i

        i += 1

assertions.assert_equals(4, maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))
assertions.assert_equals(3, maximumToys([3, 7, 2, 9, 4], 15))
assertions.assert_equals(3, maximumToys([1, 2, 3, 4], 7))

