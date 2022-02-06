def exec_command(r, c, command):
    match command:
        case 'U':
            if r > 0:
                r -= 1
        case 'D':
            if r < 2:
                r += 1
        case 'L':
            if c > 0:
                c -= 1
        case 'R':
            if c < 2:
                c += 1
    return r, c


def exec_p2_command(r, c, matrix, command):
    old_r, old_c = r, c
    match command:
        case 'U':
            r -= 1
        case 'D':
            r += 1
        case 'L':
            c -= 1
        case 'R':
            c += 1
    try:
        if matrix[r][c] is not None:
            return r, c
        else:
            return old_r, old_c
    except:
        return old_r, old_c


def q1():
    with open('day 02\input.txt', 'r') as f:
        input = f.read().splitlines()

    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    output = ''
    r, c = (1, 1)
    for line in input:
        for command in line:
            r, c = exec_command(r, c, command)
        output += str(keypad[r][c])
    return output


def q2():
    with open('day 02\input.txt', 'r') as f:
        input = f.read().splitlines()

    keypad = [
        [None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, 'A', 'B', 'C', None],
        [None, None, 'D', None, None]
    ]

    output = ''
    r, c = (1, 1)
    for line in input:
        for command in line:
            r, c = exec_p2_command(r, c, keypad, command)
        output += str(keypad[r][c])
    return output


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
