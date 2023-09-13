from collections import deque


def solution(maps):
    answer = 0
    x_len, y_len = len(maps), len(maps[0])

    # 상  하  좌  우
    pos_x = [-1, 1, 0, 0]
    pos_y = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + pos_x[i]
                ny = y + pos_y[i]

                if nx >= x_len or ny >= y_len or nx < 0 or ny < 0 or maps[nx][ny] == 0:
                    continue

                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))

        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0, 0)
    return -1 if answer == 1 else answer
