def solution(n, words):
    answer = [0, 0]
    s = set()

    for idx, word in enumerate(words):
        if idx > 0 and word[0] != words[idx-1][-1]:
            answer[0] = (idx % n) + 1
            answer[1] = (idx//n) + 1
            break
        if word not in s:
            s.add(word)
        else:
            answer[0] = (idx % n) + 1
            answer[1] = (idx//n) + 1
            break
    return answer
