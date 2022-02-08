from string import ascii_lowercase
from itertools import permutations


def all_possible_abbas():
    return [''.join(p)+''.join(p[::-1]) for p in permutations(ascii_lowercase, 2)]


def all_possible_abas():
    return [''.join(p)+p[0] for p in permutations(ascii_lowercase, 2)]


def get_bab(aba):
    return aba[1] + aba[0] + aba[1]


abbas = all_possible_abbas()
abas = all_possible_abas()


def split_ip(ip, idx):
    ip = ip.replace('[', '_')
    ip = ip.replace(']', '_')
    return '_'.join(ip.split('_')[idx::2])


def abba_outside_of_hyper(ip):
    ip = split_ip(ip, 0)
    return any(abba in ip for abba in abbas)


def abba_in_hyper(ip):
    ip = split_ip(ip, 1)
    return any(abba in ip for abba in abbas)


def q1():
    with open('day 07\input.txt', 'r') as f:
        input = f.read().splitlines()
    return len([ip for ip in input if abba_outside_of_hyper(ip) and not abba_in_hyper(ip)])


def has_aba(ip):
    super = split_ip(ip, 0)
    hyper = split_ip(ip, 1)
    return any(aba in super and get_bab(aba) in hyper for aba in abas)


def q2():
    with open('day 07\input.txt', 'r') as f:
        input = f.read().splitlines()
    return len([ip for ip in input if has_aba(ip)])


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
