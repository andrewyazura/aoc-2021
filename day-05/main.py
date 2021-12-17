import re
from collections import Counter
from itertools import cycle

with open("day-05/input.txt", "r") as file:
    puzzle_input = [
        [int(n) for n in re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", line.strip())[0]]
        for line in file.readlines()
    ]


def part_1(puzzle_input, diagonals=False):
    counter = Counter()

    for line in puzzle_input:
        x1, y1, x2, y2 = line

        if not diagonals and x1 != x2 and y1 != y2:
            continue

        xstep = 1 if x1 <= x2 else -1
        xs = range(x1, x2 + xstep, xstep)

        ystep = 1 if y1 <= y2 else -1
        ys = range(y1, y2 + ystep, ystep)

        if len(xs) < len(ys):
            xs = cycle(xs)
        else:
            ys = cycle(ys)

        counter.update(zip(xs, ys))

    return len([crossings for crossings in counter.values() if crossings > 1])


part_2 = lambda inp: part_1(inp, True)

print(part_1(puzzle_input))
print(part_2(puzzle_input))
