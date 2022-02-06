def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def q1():
    with open('day 03\input.txt', 'r') as f:
        input = f.read().splitlines()

    count = 0
    for triplet in input:
        a, b, c = [int(x) for x in triplet.split()]
        if is_triangle(a, b, c):
            count += 1
    return count


def q2():
    with open('day 03\input.txt', 'r') as f:
        input = f.read().splitlines()

    list_1, list_2, list_3 = list(), list(), list()

    for triplet in input:
        a, b, c = [int(x) for x in triplet.split()]
        list_1.append(a)
        list_2.append(b)
        list_3.append(c)

    count = 0
    for i in range(0, len(list_1), 3):
        a, b, c = list_1[i:i+3]
        if is_triangle(a, b, c):
            count += 1

    for i in range(0, len(list_2), 3):
        a, b, c = list_2[i:i+3]
        if is_triangle(a, b, c):
            count += 1

    for i in range(0, len(list_3), 3):
        a, b, c = list_3[i:i+3]
        if is_triangle(a, b, c):
            count += 1

    return count


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
