from copy import deepcopy

with open("day-04/input.txt", "r") as file:
    numbers = [int(i) for i in file.readline().split(",")]
    boards = [
        [[int(i) for i in row.split()] for row in board.strip().split("\n")]
        for board in file.read().strip().split("\n\n")
    ]


def find_first(numbers, boards, mark=False):
    check = lambda l: all(map(lambda n: n is mark, l))

    for number in numbers:
        for index, board in enumerate(boards):
            for row in board:
                for i, v in enumerate(row):
                    if v == number:
                        row[i] = mark

                        col = list(zip(*board))[i]
                        if check(row) or check(col):
                            return index, number, boards


def part_1(numbers, boards):
    boards = deepcopy(boards)

    i, n, _ = find_first(numbers, boards)
    return sum(sum(boards[i], [])) * n


def part_2(numbers, boards):
    boards = deepcopy(boards)

    while len(boards) > 1:
        i, n, boards = find_first(numbers, boards)
        boards.pop(i)

    i, n, boards = find_first(numbers, boards)

    return sum(sum(boards[i], [])) * n


print(part_1(numbers, boards))
print(part_2(numbers, boards))
