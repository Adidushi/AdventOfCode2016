from itertools import islice, takewhile


def find_next_command(current_string):
    start_idx = current_string.index('(')
    end_idx = current_string.index(')')
    amount_of_chars, replications = current_string[start_idx+1:end_idx].split(
        'x')
    return start_idx, end_idx, int(amount_of_chars), int(replications)


def q1():
    with open('day 09\input.txt', 'r') as f:
        input = f.read().strip()

    current_string = input

    start_idx, end_idx, amount_of_chars, replications = find_next_command(
        current_string)
    final_string = len(current_string[:start_idx])
    current_string = current_string[start_idx:]

    while '(' in current_string:
        start_idx, end_idx, amount_of_chars, replications = find_next_command(
            current_string)
        shit_to_add = current_string[end_idx +
                                     1:end_idx+1+amount_of_chars] * replications
        final_string += len(current_string[:start_idx] + shit_to_add)
        current_string = current_string[end_idx+1+amount_of_chars:]
    final_string += len(current_string)

    return final_string


def recursive_decompress(current_string):
    answer = 0
    chars = iter(current_string)
    for char in chars:
        if char == '(':
            n, m = map(
                int, [''.join(takewhile(lambda c: c not in 'x)', chars)) for _ in (0, 1)])
            s = ''.join(islice(chars, n))
            answer += recursive_decompress(s)*m
        else:
            answer += 1
    return answer


def q2():
    with open('day 09\input.txt', 'r') as f:
        input = f.read().strip()
    return recursive_decompress(input)


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
