#!/usr/bin/env python3

import sys

from icecream import ic

from common import get_lines, parse_args, set_debug

digit_mapping_part_1 = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

digit_mapping_part_2 = {
    "one": 1, "1": 1,
    "two": 2, "2": 2,
    "three": 3, "3": 3,
    "four": 4, "4": 4,
    "five": 5, "5": 5,
    "six": 6, "6": 6,
    "seven": 7, "7": 7,
    "eight": 8, "8": 8,
    "nine": 9, "9": 9,
}


def get_digit(sub_string: str,
              digit_mapping: dict[str, int]) -> int:
    for k, v in digit_mapping.items():
        if sub_string.startswith(k):
            return v
    return 0


def find_first_digit_from_start(input_string: str,
                                digit_mapping: dict[str, int]) -> int:
    for i in range(len(input_string)):
        d = get_digit(input_string[i:], digit_mapping)
        if d != 0:
            return d
    raise SystemExit("Cannot find first digit from start")


def find_first_digit_from_end(input_string: str,
                              digit_mapping: dict[str, int]) -> int:
    for i in range(len(input_string), -1, -1):
        d = get_digit(input_string[i:], digit_mapping)
        if d != 0:
            return d
    raise SystemExit("Cannot find first digit from end")


def main():
    args = parse_args()
    set_debug(args.debug)
    lines = ic(get_lines(args.input))

    if args.part == 1:
        digit_mapping = digit_mapping_part_1
    else:
        digit_mapping = digit_mapping_part_2
    ic(digit_mapping)
    sum = 0
    for line in lines:
        ic(line)
        sd = ic(find_first_digit_from_start(line, digit_mapping))
        ed = ic(find_first_digit_from_end(line, digit_mapping))
        sum += ic(sd * 10 + ed)
    print(sum)


if __name__ == "__main__":
    sys.exit(main())
