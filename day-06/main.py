with open("day-06/input.txt", "r") as file:
    puzzle_input = [int(i) for i in file.readline().strip().split(",")]


def spawn_fish(initial_state, days):
    buckets = [0] * 9

    for fish in initial_state:
        buckets[fish] += 1

    for day in range(days):
        i = day % 9
        n = (i + 7) % 9

        buckets[n] += buckets[i]

    return sum(buckets)


part_1 = lambda inp: spawn_fish(inp, 80)
part_2 = lambda inp: spawn_fish(inp, 256)

print(part_1(puzzle_input))
print(part_2(puzzle_input))
