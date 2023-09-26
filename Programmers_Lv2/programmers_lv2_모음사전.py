from itertools import product


def solution(word):
    answer = 0

    words = ['A', 'E', 'I', 'O', 'U']

    arr = list()
    for j in range(1, 6):
        for i in product(words, repeat=j):
            arr.append(list(i))

    arr.sort()

    for i, v in enumerate(arr):
        if word == ''.join(v):
            return (i+1)
