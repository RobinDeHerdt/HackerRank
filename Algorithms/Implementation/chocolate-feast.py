# https://www.hackerrank.com/challenges/chocolate-feast/problem
from Testing import assertions
import math

# Complete the chocolate_feast function below.
# n: an integer representing Bobby's initial amount of money
# c: an integer representing the cost of a chocolate bar
# m: an integer representing the number of wrappers he can turn in for a free bar
def chocolate_feast(n, c, m):
    bars = math.floor(n / c)

    # Initial bars eaten.
    total_bars = bars

    return trade_in_wrappers(bars, m, total_bars)

def trade_in_wrappers(wrappers, m, total_bars):
    if wrappers < m:
        return total_bars
    else:
        bars = math.floor(wrappers / m)
        wrappers_left = (wrappers % m) + bars

        total_bars += bars

        return trade_in_wrappers(wrappers_left, m, total_bars)

assertions.assert_equals(6, chocolate_feast(10, 2, 5))
assertions.assert_equals(3, chocolate_feast(12, 4, 4))
assertions.assert_equals(5, chocolate_feast(6, 2, 2))
