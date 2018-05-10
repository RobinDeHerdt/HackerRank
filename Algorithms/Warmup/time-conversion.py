#!/bin/python3

import os
import sys

from datetime import datetime


def timeConversion(s):
    d = datetime.strptime(s, "%I:%M:%S%p")
    return d.strftime("%H:%M:%S")


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
