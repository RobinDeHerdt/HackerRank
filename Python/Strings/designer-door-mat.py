# https://www.hackerrank.com/challenges/designer-door-mat
if __name__ == '__main__':

    import math

    def draw(n, m):
        middle = math.floor(n / 2)
        middle_text = "WELCOME"

        for index, value in enumerate(range(middle, 0, -1)):
            print("---" * value + ".|" + (index * 2 * "..|") + "." + "---" * value)

        remainder = int((m - len(middle_text)) / 2)
        print("-" * remainder + middle_text + "-" * remainder)

        for index, value in enumerate(range(1, middle + 1)):
            print("---" * value + ".|" + (((middle - index - 1) * 2) * "..|") + "." + "---" * value)

    draw(7, 21)
    print("\n")
    draw(9, 27)
    print("\n")
    draw(11, 33)