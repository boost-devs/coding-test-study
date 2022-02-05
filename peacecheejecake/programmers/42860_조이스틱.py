def num_to_correct(target):
    target = ord(target)
    return min(target - ord('A'), 1 + ord('Z') - target)


def solution(name):
    vert = sum(map(num_to_correct, name))

    a_chunks = []
    idx = []
    for i, c in enumerate(name):
        if c == 'A':
            if not idx:
                idx.append(i)
            if i == len(name) - 1 or name[i + 1] != 'A':
                idx.append(i)
                a_chunks.append(idx)
                idx = []

    horz = len(name) - 1
    for s, e in a_chunks:
        if s == 0:
            dist = len(name) - e - 1
        elif e == len(name) - 1:
            dist = s - 1
        else:
            dist = min(
                2 * (s - 1) + (len(name) - 1 - e),
                2 * (len(name) - 1 - e) + (s - 1),
            )
        horz = min(horz, dist)

    return vert + horz
