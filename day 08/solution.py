from dataclasses import dataclass


@dataclass
class Grid:
    grid = set()

    def rect(self, w, h):
        for r in range(h):
            for c in range(w):
                self.grid.add((r, c))

    def rotate(self, axis, query, amount):
        points_to_remove = set()
        points_to_add = set()

        if axis == 'row':
            for point in self.grid:
                if point[0] == query:
                    points_to_remove.add(point)
                    points_to_add.add((point[0], (point[1] + amount)%50))
        elif axis == 'column':
            for point in self.grid:
                if point[1] == query:
                    points_to_remove.add(point)
                    points_to_add.add(((point[0] + amount)%6, point[1]))

        self.grid -= points_to_remove
        self.grid.update(points_to_add)


def parse_command(line):
    splat = line.split(' ')
    command_type = splat[0]
    if command_type == 'rect':
        size = splat[1].split('x')
        return Grid.rect, int(size[0]), int(size[1])
    elif command_type == 'rotate':
        axis = splat[1]
        query = int(splat[2].split('=')[1])
        amount = int(splat[4])
        return Grid.rotate, axis, query, amount


def q1():
    with open('day 08\input.txt', 'r') as f:
        input = f.read().splitlines()

    grid = Grid()
    for line in input:
        command, *args = parse_command(line)
        command(grid, *args)
    return len(grid.grid)

def print_matrix(grid):
    for line in grid:
        print(''.join(line))

def q2():
    with open('day 08\input.txt', 'r') as f:
        input = f.read().splitlines()

    grid = Grid()
    for line in input:
        command, *args = parse_command(line)
        command(grid, *args)


    x = [[' ' for i in range(50)] for j in range(6)]
    for point in grid.grid:
        x[5-point[0]][point[1]] = '█'
    print_matrix(x)


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
