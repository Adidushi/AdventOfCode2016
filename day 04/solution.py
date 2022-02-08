from dataclasses import dataclass
from collections import Counter


@dataclass
class Room:
    name: str
    sector_id: int
    checksum: str

    def is_valid(self):
        name = self.name.replace(' ', '')
        most_common_letters = [letter for letter, _ in sorted(
            Counter(name).most_common(10), key=lambda x: (-x[1], x[0]))][:5]
        return self.checksum == ''.join(most_common_letters)

    def get_sector(self):
        return self.sector_id if self.is_valid() else 0

    def rotate(self):
        rot = self.sector_id % 26
        return ''.join(chr(((ord(letter) - ord('a') + rot) % 26) + ord('a')) for letter in self.name)


def parse_room(line):
    *name, rest = line.split('-')
    sector_id, checksum = rest[:-1].split('[')
    name = ' '.join(name)
    sector_id = int(sector_id)

    return Room(name, sector_id, checksum)


def q1():
    with open('day 04\input.txt', 'r') as f:
        input = f.read().splitlines()

    rooms = [parse_room(line) for line in input]
    return sum(room.get_sector() for room in rooms)


def q2():
    with open('day 04\input.txt', 'r') as f:
        input = f.read().splitlines()

    rooms = [parse_room(line) for line in input]
    return [room.sector_id for room in rooms if room.is_valid() and 'pole' in room.rotate()]


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
