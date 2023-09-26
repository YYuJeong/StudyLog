def convert(num, base):
    tmp = '0123456789ABCDEF'
    a, b = divmod(num, base)
    result = ''
    if a == 0:
        return tmp[b]
    else:
        return convert(a, base) + tmp[b]


def solution(n, t, m, p):
    answer = ''
    result = ''

    for i in range(t*m):
        result += convert(i, n)
        print(result)
    for i in range(t):
        answer += result[m*i+(p-1)]
    return answer
