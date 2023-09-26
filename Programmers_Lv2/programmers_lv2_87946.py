from itertools import permutations


def solution(k, dungeons):
    answer = 0

    all_dungeons = []
    for i in permutations(dungeons, len(dungeons)):
        all_dungeons.append(list(i))

    possible = []
    for dungeons in all_dungeons:
        stemina = k
        cnt = 0
        for i, dungeon in enumerate(dungeons):
            if dungeon[0] <= stemina:
                stemina -= dungeon[1]
                cnt += 1
            elif dungeon[0] > stemina:
                break
            possible.append(cnt)

    answer = max(possible)
    return answer
