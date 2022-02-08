from hashlib import md5


def get_password(inital):
    final_str = ''
    i = 0
    while len(final_str) < 8:
        i += 1
        hash = md5((inital + str(i)).encode('utf-8')).hexdigest()
        if hash[:5] == '00000':
            print(hash)
            yield hash[5]
            final_str += hash[5]


def q1():
    input = 'ugkcyxxp'
    return ''.join(list(get_password(input)))


def get_ordered_password(inital):
    final_str = [''] * 8
    i = 0
    while '' in final_str:
        i += 1
        hash = md5((inital + str(i)).encode('utf-8')).hexdigest()
        if hash[:5] == '00000' and hash[5] in ('0', '1', '2', '3', '4', '5', '6', '7'):
            print(hash)
            loc, val = int(hash[5]), hash[6]
            if final_str[loc] == '':
                final_str[loc] = val

    return ''.join(final_str)


def q2():
    input = 'ugkcyxxp'
    return get_ordered_password(input)


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    # print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
