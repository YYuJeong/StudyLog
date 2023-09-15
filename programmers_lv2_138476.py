from collections import Counter


def solution(k, tangerine):
    dic = dict(Counter(tangerine))
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    answer = 0
    sum = 0
    if dic[0][1] >= k:
        return 1
    else:
        for a, b in dic:
            if sum < k:
                sum += b
                answer += 1
            else:
                break
    return answer
