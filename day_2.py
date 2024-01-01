#!/usr/bin/env python3

import sys

from icecream import ic

from common import get_lines, parse_args, set_debug

import re

# Dictionary specifying cube limits for each color
cube_limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def parse_game(input_string) -> list[dict[str, int]]:
    """
    Parse the game configuration from an input string.
    in: "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    out: [
           {'blue': 3, 'red': 4},
           {'red': 1, 'green': 2, 'blue': 6},
           {'green': 2}
         ]
    """
    result_list = []
    sub_strings = ic(input_string.split(';'))
    pattern = re.compile(r'(\d+)\s+(\w+)')
    for sub_string in sub_strings:
        matches = pattern.findall(sub_string)
        result_dict = {match[1]: int(match[0]) for match in matches}
        result_list.append(result_dict)
    ic(result_list)
    return result_list


def check_cube_limit(set: dict[str, int], color: str) -> bool:
    """
    Check if the number of cubes of a specific
    color is within the limit.
    """
    cubes = set.get(color, 0)
    if cubes > cube_limits[color]:
        ic(f"Not enough {color} cubes ({cubes} > {cube_limits[color]})")
        return False
    return True


def game_is_possible(game: list[dict[str, int]]) -> bool:
    """
    Check if the game configuration is feasible based on cube limits.
    """
    for set in game:
        ic(set)
        for color in cube_limits.keys():
            if check_cube_limit(set, color) is False:
                return False
    return True


def get_min(set: dict[str, int], color: str, current_min: int) -> int:
    """
    Get the minimum count of cubes needed of a specific color.
    """
    n = set.get(color, 0)
    ic(f"color: {color}: {n} > {current_min}")
    if n > current_min:
        return n
    return current_min


def get_min_cubes(game: list[dict[str, int]]) -> int:
    """
    Calculate the product of minimum cube counts
    for each color in the game.
    """
    min_blue, min_red, min_green = 0, 0, 0
    for set in game:
        ic(set)
        min_blue = ic(get_min(set, "blue", min_blue))
        min_red = ic(get_min(set, "red", min_red))
        min_green = ic(get_min(set, "green", min_green))
    return ic(min_blue * min_red * min_green)


def main():
    args = parse_args()
    set_debug(args.debug)
    lines = ic(get_lines(args.input))

    id = 1
    res = 0
    for line in lines:
        ic(line)
        game = ic(parse_game(line))

        if args.part == 1:
            if game_is_possible(game):
                res += id
        else:
            res += get_min_cubes(game)
        id += 1

    print(res)


if __name__ == "__main__":
    sys.exit(main())
