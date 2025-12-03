import argparse
from itertools import chain
import re
from pathlib import Path

PROD = True

def load_input():
    return (Path() / "input.txt").read_text()

TEST_INPUT = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""

INPUT = load_input() if PROD else TEST_INPUT


def part_1() -> str:
    def _f(l: list[tuple[int, int]] = []) -> str:
        _sum = 0
        for i in chain.from_iterable(range(s,e+1) for s,e in l):
            if len(str(i)) % 2 == 0:
                _sum += i if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:] else 0

        return str(_sum)

    return (_f([(int(s), int(e)) for s,e in re.findall(r"(\d+)-(\d+)", INPUT)]))

def part_2() -> str:
    raise NotImplementedError


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('part', type=int, choices=(1,2))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    parts = {
        1: part_1,
        2: part_2,
    }

    print(f"Day: {int(Path().parent.name)} Part: {args.part}")
    print(parts[args.part]())

if __name__ == "__main__":
    main()
