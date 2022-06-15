from dataclasses import dataclass


@dataclass
class Disc:
    positions: int
    start_position: int
    index: int

    def calc_position(self, time):
        return (self.start_position + time + self.index + 1) % self.positions


def q1():
    with open('day 15\input.txt', 'r') as f:
        input = f.read().splitlines()
    discs = list()
    for index, line in enumerate(input):
        positions, start_position = int(line.split(
            ' ')[3]), int(line[:-1].split(' ')[-1])
        discs.append(Disc(positions, start_position, index))

    time = 0
    while True:
        if all(disc.calc_position(time) == 0 for disc in discs):
            return time
        time += 1


def q2():
    with open('day 15\input.txt', 'r') as f:
        input = f.read().splitlines()

    discs = list()
    for index, line in enumerate(input):
        positions, start_position = int(line.split(
            ' ')[3]), int(line[:-1].split(' ')[-1])
        discs.append(Disc(positions, start_position, index))

    discs.append(Disc(11, 0, len(discs)))

    time = 0
    while True:
        if all(disc.calc_position(time) == 0 for disc in discs):
            return time
        time += 1


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
