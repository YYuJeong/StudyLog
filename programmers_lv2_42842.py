def solution(brown, yellow):
    total = brown + yellow

    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            if (i+2) * ((yellow//i) + 2) == total:
                return [(yellow//i) + 2, i+2]
