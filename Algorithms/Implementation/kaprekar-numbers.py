# https://www.hackerrank.com/challenges/kaprekar-numbers/problem
def kaprekarNumbers(p, q):

    result = []
    for n in range(p, q + 1):
        d = len(str(n))
        number = str(pow(n, 2))

        r = number[d*-1:]
        l = number[:d*-1]

        if not l:
            l = 0

        if int(l) + int(r) == int(n):
            result.append(str(n))

    if result:
        print(" ".join(result))
    else:
        print("INVALID RANGE")
