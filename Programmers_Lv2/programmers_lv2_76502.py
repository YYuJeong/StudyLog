def solution(s):
    cnt = 0
    for i in range(len(s)):
        s_left = s[i:] + s[:i]
        while True:
            s_len = len(s_left)
            s_left = s_left.replace("()", '')
            s_left = s_left.replace('{}', '')
            s_left = s_left.replace('[]', '')

            if s_left == '':
                cnt += 1
                break
            if len(s_left) == s_len:
                break

    return cnt
