def solution(n):
    answer = 0

    run = [0] * 2000

    run[0] = 1
    run[1] = 1
    for i in range(2, n+1):
        if run[i] == 0:
            run[i] = run[i-1] + run[i-2]

    return run[n] % 1234567
