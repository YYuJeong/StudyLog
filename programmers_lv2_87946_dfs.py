answer = 0


def DFS(k, cnt, dungeon, check):
    global answer
    answer = max(answer, cnt)

    for i in range(len(dungeon)):
        if check[i] == 0 and k >= dungeon[i][0]:
            check[i] = 1
            DFS(k-dungeon[i][1], cnt+1, dungeon, check)
            check[i] = 0


def solution(k, dungeons):
    global answer
    check = [0]*len(dungeons)

    DFS(k, 0, dungeons, check)
    return answer
