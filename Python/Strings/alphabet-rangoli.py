# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
import string

def draw(n):
    alphabet = list(string.ascii_lowercase)
    letters = alphabet[0:n]

    line_width  = (n * 2 - 1) * 2 - 1

    # Build the first part of the image.
    for i in range(n - 1, 0, -1):
        chunked_letters = letters[i:len(letters)]
        # print(selected_letters)
        renderLine(chunked_letters, line_width)

    # Build the center part of the image.
    renderLine(letters, line_width)

    # Build the first part of the image.
    for i in range(0, n - 1):
        chunked_letters = letters[i:len(letters)]
        renderLine(chunked_letters, line_width)


def renderLine(letters, line_width):

    # Build the first part of the line, including the center letter.
    letters.reverse()
    result = '-'.join(letters)

    # Build the second part of the line, remove the center letter
    # and join first & last line.
    letters.reverse()
    del letters[0]

    # Only add this one if we're not on the first or last line.
    if letters:
        result += '-'

    result += '-'.join(letters)

    rest = line_width - len(result)
    remainder = int(rest / 2) * '-'

    print(remainder + result + remainder)

draw(3)
print("\n")
draw(5)
print("\n")
draw(10)
print("\n")
draw(26)
print("\n")
