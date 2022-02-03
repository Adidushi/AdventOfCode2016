def parse_input(input):
    directions = input.split(', ')
    return directions


def right(old_direction):
    match old_direction:
        case (0, 1):
            return (1, 0)
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)
        case (-1, 0):
            return (0, 1)


def left(old_direction):
    match old_direction:
        case (0, 1):
            return (-1, 0)
        case (-1, 0):
            return (0, -1)
        case (0, -1):
            return (1, 0)
        case (1, 0):
            return (0, 1)


def turn_direction(old_direction, turn):
    match turn:
        case 'L':
            return left(old_direction)
        case 'R':
            return right(old_direction)


def move_distance(old_position, direction, distance):
    return old_position[0] + direction[0] * distance, old_position[1] + direction[1] * distance


def all_between(coord_1, coord_2):
    x_range = range(min(coord_1[0], coord_2[0]),
                    max(coord_1[0], coord_2[0]) + 1)
    y_range = range(min(coord_1[1], coord_2[1]),
                    max(coord_1[1], coord_2[1]) + 1)
    return set((x, y) for x in x_range for y in y_range)


def q1():
    with open('day 01\input.txt', 'r') as f:
        input = parse_input(f.read())

    position = (0, 0)
    direction = (0, 1)
    for command in input:
        dir = command[0]
        dist = command[1:]
        direction = turn_direction(direction, dir)
        position = move_distance(position, direction, int(dist))

    return sum(abs(c) for c in position)


def q2():
    with open('day 01\input.txt', 'r') as f:
        input = parse_input(f.read())

    position = (0, 0)
    visited = set()
    direction = (0, 1)
    for command in input:
        dir = command[0]
        dist = command[1:]
        direction = turn_direction(direction, dir)
        old_pos, position = position, move_distance(
            position, direction, int(dist))
        betweeners = all_between(old_pos, position)
        for coord in betweeners:
            if coord in visited:
                return sum(abs(c) for c in coord)
        visited.update(all_between(old_pos, position))
        visited.remove(position)


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
