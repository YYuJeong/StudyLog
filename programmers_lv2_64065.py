def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s = list(map(lambda t: t.split(','), s))

    s_sorted = sorted(s, key=len)

    for s in s_sorted:
        for num in s:
            if int(num) not in answer:
                answer.append(int(num))
    return answer
