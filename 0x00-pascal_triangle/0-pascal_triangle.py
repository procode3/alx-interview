#!/usr/bin/python3
"""a function to create pascal's triangle"""


def pascal_triangle(n):
    """creation of pascal's triangle"""
    base = []
    if n == 1:
        return [[1]]
    for i in range(n - 1):
        if len(base) > 0:
            last = base[-1]
        else:
            last = [1]
            base.append(last)
        next = [1]
        for i in range(len(last) - 1):
            next.append(last[i] + last[i + 1])
        next.append(1)
        base.append(next)

    return base
