#!/bin/python3


def print_logo(thickness):
    base_char = 'H'

    # Top Cone
    for i in range(thickness):
        print((base_char * i).rjust(thickness - 1) + base_char + (base_char * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((base_char * thickness).center(thickness * 2) + (base_char * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((base_char * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for i in range(thickness + 1):
        print((base_char * thickness).center(thickness * 2) + (base_char * thickness).center(thickness * 6))

    # Bottom Cone
    for i in range(thickness):
        print(((base_char * (thickness - i - 1)).rjust(thickness) + base_char + (base_char * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))


if __name__ == '__main__':
    thickness = int(input())  # This must be an odd number

    print_logo(thickness)
