with open("day-02/input.txt", "r") as file:
    puzzle_input = [i.split() for i in file.readlines()]


def part_1(puzzle_input):
    depth = 0
    horizontal = 0

    for command, value in puzzle_input:
        value = int(value)
        if command == "forward":
            horizontal += value

        elif command == "up":
            depth -= value

        elif command == "down":
            depth += value

    return depth * horizontal


def part_2(puzzle_input):
    aim = 0
    depth = 0
    horizontal = 0

    for command, value in puzzle_input:
        value = int(value)
        if command == "forward":
            horizontal += value
            depth += aim * value

        elif command == "up":
            aim -= value

        elif command == "down":
            aim += value

    return depth * horizontal


print(part_1(puzzle_input))
print(part_2(puzzle_input))
