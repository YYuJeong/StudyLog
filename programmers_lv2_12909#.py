def solution(s):
    answer = True
    stack = []
    for c in s:
        if c == '(':
            stack.append('(')
        else:
            if stack == []:
                return False
            else:
                stack.pop()

    return stack == []
