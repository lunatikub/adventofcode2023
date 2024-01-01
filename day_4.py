#!/usr/bin/env python3

import sys

from icecream import ic

from common import get_lines, parse_args, set_debug


def parse_card(card: str) -> list[list[int]]:
    """
    Parse the game configuration from an input string.
    in: Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    out: {'Card 1': [[41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]]}
    """
    card_parts = card.split(':')
    numbers_part = card_parts[1].strip()
    numbers_lists = [list(map(int, part.strip().split()))
                     for part in numbers_part.split('|')]
    return numbers_lists


def get_matching_numbers(winning_numbers: list[int],
                         numbers: list[int]) -> int:
    """
    Counts how many elements from the second list 'numbers' are also present
    in the first list 'winning_numbers', and returns this count.
    """
    nr_matching = 0
    for number in numbers:
        if number in winning_numbers:
            nr_matching += 1
    return nr_matching


def main():
    args = parse_args()
    set_debug(args.debug)
    lines = ic(get_lines(args.input))

    if args.part == 2:
        # Create a dictionary with len(lines) members,
        # each associated with a unique ID and a value of 1.
        instances = {i: 1 for i in range(1, len(lines) + 1)}
        ic(instances)

    points = 0
    card_id = 1
    for line in lines:
        cards = parse_card(line)
        winning_numbers = cards[0]
        numbers = cards[1]
        ic(card_id)
        nr_matching = ic(get_matching_numbers(winning_numbers, numbers))
        if args.part == 1:
            points += ic(int(pow(2, nr_matching - 1)))
        else:
            for id in range(card_id + 1, card_id + 1 + nr_matching):
                instances[id] += instances[card_id]
            ic(instances)
        card_id += 1

    if args.part == 1:
        print(points)
    else:
        print(sum(instances.values()))


if __name__ == "__main__":
    sys.exit(main())
