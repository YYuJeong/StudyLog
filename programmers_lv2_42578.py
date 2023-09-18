from collections import defaultdict


def solution(clothes):
    dic = defaultdict(list)

    for c in clothes:
        dic[c[1]].append(c[0])

    answer = 1
    for d in dic:
        answer *= (len(dic[d]) + 1)

    return answer-1
