from dataclasses import dataclass


@dataclass
class Computer:
    registers: dict

    def parse_command(self, command):
        command = command.split()
        if command[0] == 'cpy':
            return self.cpy(command[1], command[2])

        if command[0] == 'inc':
            return self.inc(command[1])

        if command[0] == 'dec':
            return self.dec(command[1])

        if command[0] == 'jnz':
            return self.jnz(command[1], command[2])

    def cpy(self, value, register):
        if value.isnumeric():
            self.registers[register] = int(value)
        else:
            self.registers[register] = self.registers[value]

    def inc(self, register):
        self.registers[register] += 1

    def dec(self, register):
        self.registers[register] -= 1

    def jnz(self, value, jump):
        if value.isnumeric():
            if int(value) != 0:
                return int(jump)
        else:
            if self.registers[value] != 0:
                return int(jump)


def q1():
    with open('day 12\input.txt', 'r') as f:
        input = f.read().splitlines()

    computer = Computer({'a': 0, 'b': 0, 'c': 0, 'd': 0})
    i = 0
    while i < len(input):
        command = input[i]
        jump = computer.parse_command(command)
        if jump:
            i += jump
        else:
            i += 1

    return computer.registers['a']


def q2():
    with open('day 12\input.txt', 'r') as f:
        input = f.read().splitlines()

    computer = Computer({'a': 0, 'b': 0, 'c': 1, 'd': 0})
    i = 0
    while i < len(input):
        command = input[i]
        jump = computer.parse_command(command)
        if jump:
            i += jump
        else:
            i += 1

    return computer.registers['a']


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
