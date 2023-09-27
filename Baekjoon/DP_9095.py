# f(n) = f(n-3) + f(n-2) + f(n-1) n>3
T = int(input())


def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return dp(n-3) + dp(n-2) + dp(n-1)


for i in range(T):
    n = int(input())
    print(dp(n))
