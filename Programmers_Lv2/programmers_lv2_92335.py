def check(num):
    num = int(num)
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    rev_base = ''

    while n > 0:
        n, res = divmod(n, k)
        rev_base += str(res)

    rev_base = rev_base[::-1]
    prime = ''
    for i in range(len(rev_base)):
        if rev_base[i] != '0':
            prime += rev_base[i]
        else:
            if prime != '':
                if check(prime):
                    answer += 1
                prime = ''
    if prime != '':
        if check(prime):
            answer += 1

    return answer
