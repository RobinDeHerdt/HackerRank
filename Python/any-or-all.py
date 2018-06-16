#!/bin/python3

n, arr = int(input()), input().split()
print(all([int(i) > 0 for i in arr]) and any([j == j[::-1] for j in arr]))
