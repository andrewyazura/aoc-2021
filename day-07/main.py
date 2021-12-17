with open("day-07/input.txt", "r") as file:
    puzzle_input = [int(i) for i in file.readline().strip().split(",")]


def part_1(puzzle_input):
    return min(
        [
            sum([abs(position - crab) for crab in puzzle_input])
            for position in range(
                min(puzzle_input), int(sum(puzzle_input) / len(puzzle_input)) + 1
            )
        ]
    )


def get_fuel(steps):
    return steps * (steps + 1) // 2


def part_2(puzzle_input):
    return min(
        [
            sum([get_fuel(abs(position - crab) + 1) for crab in puzzle_input])
            for position in range(
                min(puzzle_input), int(sum(puzzle_input) / len(puzzle_input)) + 1
            )
        ]
    )


print(part_1(puzzle_input))
print(part_2(puzzle_input))
