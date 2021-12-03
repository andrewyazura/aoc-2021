with open("day-03/input.txt", "r") as file:
    puzzle_input = [i.strip() for i in file.readlines()]


def part_1(puzzle_input):
    gamma = ""
    epsilon = ""

    for col in zip(*puzzle_input):
        ratio = col.count("1") / len(col)

        if ratio >= 0.5:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)


def part_2(puzzle_input):
    oxygen = puzzle_input
    co2 = puzzle_input

    for i in range(len(puzzle_input[0])):
        oxygen_col = [value[i] for value in oxygen]
        oxygen_ratio = oxygen_col.count("1") / len(oxygen_col)

        co2_col = [value[i] for value in co2]
        co2_ratio = co2_col.count("1") / len(co2_col)

        if len(oxygen) > 1:
            if oxygen_ratio >= 0.5:
                oxygen = [value for value in oxygen if value[i] == "1"]
            else:
                oxygen = [value for value in oxygen if value[i] == "0"]

        if len(co2) > 1:
            if co2_ratio >= 0.5:
                co2 = [value for value in co2 if value[i] == "0"]
            else:
                co2 = [value for value in co2 if value[i] == "1"]

    return int(oxygen[0], 2) * int(co2[0], 2)


print(part_1(puzzle_input))
print(part_2(puzzle_input))
