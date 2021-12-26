with open("day-25/input.txt", "r") as file:
    puzzle_input = [[char for char in row.strip()] for row in file.readlines()]


width = len(puzzle_input[0])
height = len(puzzle_input)


def get_coords(x, y, width, height):
    return x % width, y % height


def move_char(matrix, char, dx=0, dy=0):
    movable = [
        (x, y)
        for y in range(height)
        for x in range(width)
        if matrix[y][x] == char and matrix[(y + dy) % height][(x + dx) % width] == "."
    ]

    for point in movable:
        x, y = point
        matrix[y][x] = "."
        matrix[(y + dy) % height][(x + dx) % width] = char

    return len(movable)


def part_1(puzzle_input):
    counter = 0

    while True:
        east_movable = move_char(puzzle_input, ">", dx=1)
        south_movable = move_char(puzzle_input, "v", dy=1)
        counter += 1

        if east_movable + south_movable == 0:
            break

    return counter


print(part_1(puzzle_input))
