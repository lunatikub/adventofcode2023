#!/usr/bin/env python3

from argparse import ArgumentParser, Namespace

from icecream import ic


def get_lines(file_path: str) -> list[str]:
    lines = []
    with open(file_path, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('--debug',
                        action='store_true',
                        help='Enable debug mode')
    parser.add_argument('--input',
                        type=str,
                        help='Input file')
    parser.add_argument('--part',
                        type=int,
                        help='Part 1 or 2')
    args = parser.parse_args()
    return args


def set_debug(enable: bool) -> None:
    ic.disable()
    if enable:
        ic.enable()


