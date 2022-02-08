from collections import Counter


def q1():
    with open('day 06\input.txt', 'r') as f:
        input = f.read().splitlines()
    cols = zip(*input)
    return ''.join([Counter(col).most_common(1)[0][0] for col in cols])


def q2():
    with open('day 06\input.txt', 'r') as f:
        input = f.read().splitlines()
    cols = zip(*input)
    return ''.join([Counter(col).most_common()[-1][0] for col in cols])


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
