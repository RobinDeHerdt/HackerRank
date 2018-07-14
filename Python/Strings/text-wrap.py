#!/bin/python3


import textwrap


def wrap(string, max_width):
    return textwrap.fill(" ".join(textwrap.wrap(string, max_width)), max_width)

