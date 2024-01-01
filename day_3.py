#!/usr/bin/env python3

import sys
from functools import reduce
from operator import mul

from icecream import ic

from common import get_current_function_name, get_lines, parse_args, set_debug


def get_number(lines, sz, y, x) -> int:
    """
    Extracts a number from the lines[y][x] position
    by finding its start and end indices.
    """
    ic(f"{get_current_function_name()}: ({y}, {x})")
    x_start, x_end = x, x
    while x_start >= 0 and lines[y][x_start - 1].isdigit():
        x_start -= 1
    while x_end < sz and lines[y][x_end].isdigit():
        x_end += 1
    ic(f"y:{y}, x_start: {x_start}, x_end: {x_end}")
    return int(lines[y][x_start:x_end])


def get_adjacent_symbol_from_number(lines, sz, y, x_start) -> tuple[int, int]:
    """
    Try to find an adjacent symbol to a number at position lines[y][x_start].
    If found returns the number and the new x position to continue.
    """
    x_end = x_start
    while x_end < sz and lines[y][x_end].isdigit():
        x_end += 1
    n = int(lines[y][x_start:x_end])
    ic(f"y:{y}, x_start:{x_start}, x_end:{x_end}, n:{n}")
    for yy in range(y - 1, y + 2):
        if yy >= 0 and yy < sz:
            for xx in range(x_start - 1, x_end + 1):
                if xx >= 0 and xx < sz:
                    ic(yy, xx, lines[yy][xx])
                    if lines[yy][xx].isdigit() is False and lines[yy][xx] != '.':
                        return n, x_end
    ic("No symbol adjacent found...")
    return 0, x_end


def get_2_adjacent_numbers_from_star(lines, sz, y, x) -> int:
    """
    Finds two adjacent numbers around the '*' symbol at
    position lines[y][x] and calculates their product.
    """
    numbers = []
    ic(f"{get_current_function_name()}: ({y}, {x})")
    for yy in range(y - 1, y + 2):
        if yy >= 0 and yy < sz:
            for xx in range(x - 1, x + 2):
                if xx >= 0 and xx < sz:
                    if lines[yy][xx].isdigit():
                        numbers.append(get_number(lines, sz, yy, xx))
    uniq_numbers = set(numbers)
    if len(uniq_numbers) == 2:
        res = reduce(mul, uniq_numbers)
        ic(f"Two adjacent numbers found ({y},{x}): {uniq_numbers}: {res}")
        return res
    return 0


def main():
    args = parse_args()
    set_debug(args.debug)
    lines = ic(get_lines(args.input))

    sz = ic(len(lines[0]))
    y = 0
    sum = 0
    while y < sz:
        x = 0
        while x < sz:
            if args.part == 1:
                if lines[y][x].isdigit():
                    n, x = ic(get_adjacent_symbol_from_number(lines, sz, y, x))
                    sum += n
            else:
                if lines[y][x] == "*":
                    sum += get_2_adjacent_numbers_from_star(lines, sz, y, x)
            x += 1
        y += 1
    print(sum)


if __name__ == "__main__":
    sys.exit(main())
