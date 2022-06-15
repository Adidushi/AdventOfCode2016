from functools import cache
import hashlib
import re

salt = 'cuanljph'
pattern = re.compile(r'(.)\1{2,}')


@cache
def hashed(in_str, iterations=1):
    h = in_str
    for _ in range(iterations):
        h = hashlib.md5(h.encode('utf-8')).hexdigest()
    return h


@cache
def is_hash_valid(index, iterations=1):
    in_str = salt + str(index)
    hash = hashed(in_str, iterations=iterations)
    match = pattern.search(hash)
    if not match:
        return
    to_match = match.group()[0] * 5
    for index in range(index+1, index+1000):
        if to_match in hashed(salt + str(index), iterations=iterations):
            return True
    return False


def q1():
    index = 0
    found = list()
    while True:
        if is_hash_valid(index):
            found.append(index)
            if len(found) == 64:
                return index
        index += 1


def q2():
    index = 0
    found = list()
    while True:
        if is_hash_valid(index, iterations=2017):
            found.append(index)
            if len(found) == 64:
                return index
        index += 1


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
