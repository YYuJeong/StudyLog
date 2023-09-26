import itertools


def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def solution(str1, str2):
    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()

    set1 = list()
    set2 = list()
    for i in pairwise(str1):
        set1.append(i[0]+i[1])

    for i in pairwise(str2):
        set2.append(i[0]+i[1])

    # data processing 2
    tmp = [i for i in set1 if i.isalpha()]
    set1 = tmp.copy()
    tmp = [i for i in set2 if i.isalpha()]
    set2 = tmp.copy()

    # intersection
    tmp = set2.copy()
    common = []
    for i in set1:
        if (i in tmp):
            tmp.remove(i)
            common.append(i)

    total = len(set1) + len(set2) - len(common)

    if (len(set1) == 0) and (len(set2) == 0):
        answer = 1
    else:
        answer = len(common) / total

    return int(answer*65536)
