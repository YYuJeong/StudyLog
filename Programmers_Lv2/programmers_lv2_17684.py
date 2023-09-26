
def solution(msg):
    answer = [0]
    dic = {chr(i): (i-64) for i in range(65, 91)}

    w = ''
    value = 26
    for i in range(len(msg)):
        w += msg[i]
        if not w in dic:
            value += 1
            dic[w] = value

            w = msg[i]
            answer.append(dic[w])
        else:
            answer[-1] = dic[w]
    return answer
