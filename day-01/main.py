with open("day-01/input.txt", "r") as file:
    puzzle_input = [int(i.strip()) for i in file.readlines()]


def part_1(puzzle_input):
    return sum([puzzle_input[i - 1] < e for i, e in enumerate(puzzle_input)])


def part_2(puzzle_input):
    return part_1(
        [sum(i) for i in zip(puzzle_input, puzzle_input[1:], puzzle_input[2:])]
    )


print(part_1(puzzle_input))
print(part_2(puzzle_input))
