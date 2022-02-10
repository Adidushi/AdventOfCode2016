from dataclasses import dataclass


@dataclass
class Bot:
    chips: list

    def give(self, chip: int) -> None:
        self.chips.append(chip)
        self.chips = sorted(self.chips)

    def high(self):
        high = max(self.chips)
        self.chips.remove(high)
        return high

    def low(self):
        low = min(self.chips)
        self.chips.remove(low)
        return low


def parse_line(line: str) -> tuple:
    if line.startswith('value'):
        return {
            'command': 'value',
            'bot': int(line.split()[5]),
            'chip': int(line.split()[1])
        }
    elif line.startswith('bot'):
        return {
            'command': 'bot',
            'bot': int(line.split()[1]),
            'low_output': line.split()[5] == 'output',
            'low': int(line.split()[6]),
            'high_output': line.split()[-2] == 'output',
            'high': int(line.split()[-1])
        }


def check_cmp_bot(bots: dict) -> bool:
    for bot in bots.values():
        if bot.chips == [17, 61]:
            return True
    return False


def q1():
    with open('day 10\input.txt', 'r') as f:
        input = f.read().splitlines()

    values = []
    gives = []

    for line in input:
        cmd = parse_line(line)
        if cmd['command'] == 'value':
            values.append(cmd)
        elif cmd['command'] == 'bot':
            gives.append(cmd)

    outputs = dict()
    bots = dict()

    for value in values:
        if value['bot'] not in bots:
            bots[value['bot']] = Bot([value['chip']])
        else:
            bots[value['bot']].give(value['chip'])

    while not check_cmp_bot(bots):
        for give in gives:
            if give['bot'] in bots:
                if len(bots[give['bot']].chips) == 2:
                    if not give['low_output']:
                        if give['low'] not in bots:
                            bots[give['low']] = Bot([])
                        bots[give['low']].give(bots[give['bot']].low())
                    else:
                        if give['low'] not in outputs:
                            outputs[give['low']] = 0
                        outputs[give['low']] += bots[give['bot']].low()
                    if not give['high_output']:
                        if give['high'] not in bots:
                            bots[give['high']] = Bot([])
                        bots[give['high']].give(bots[give['bot']].high())
                    else:
                        if give['high'] not in outputs:
                            outputs[give['high']] = 0
                        outputs[give['high']] += bots[give['bot']].high()
                    
                    bots.pop(give['bot'])
                    break

    for bot_num, bot in bots.items():
        if bot.chips == [17, 61]:
            return bot_num


def q2():
    with open('day 10\input.txt', 'r') as f:
        input = f.read().splitlines()

    values = []
    gives = []

    for line in input:
        cmd = parse_line(line)
        if cmd['command'] == 'value':
            values.append(cmd)
        elif cmd['command'] == 'bot':
            gives.append(cmd)

    outputs = dict()
    bots = dict()

    for value in values:
        if value['bot'] not in bots:
            bots[value['bot']] = Bot([value['chip']])
        else:
            bots[value['bot']].give(value['chip'])

    while bots:
        for give in gives:
            if give['bot'] in bots:
                if len(bots[give['bot']].chips) == 2:
                    if not give['low_output']:
                        if give['low'] not in bots:
                            bots[give['low']] = Bot([])
                        bots[give['low']].give(bots[give['bot']].low())
                    else:
                        if give['low'] not in outputs:
                            outputs[give['low']] = 0
                        outputs[give['low']] += bots[give['bot']].low()

                    if not give['high_output']:
                        if give['high'] not in bots:
                            bots[give['high']] = Bot([])
                        bots[give['high']].give(bots[give['bot']].high())
                    else:
                        if give['high'] not in outputs:
                            outputs[give['high']] = 0
                        outputs[give['high']] += bots[give['bot']].high()
                    
                    bots.pop(give['bot'])
                    break

    return outputs.get(0) * outputs.get(1) * outputs.get(2)


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
