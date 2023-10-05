from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, a, b):
  q = deque()
  q.append((a, b))
  graph[a][b] = 0 #탐색 중인 부분 0으로 만들어서 다시 탐색하지 않도록 함
  cnt = 1
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        q.append((nx, ny))
        cnt += 1
  return cnt

paint = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      paint.append(bfs(graph, i, j))

if len(paint) == 0:
  print(len(paint))
  print(0)
else:
  print(len(paint))
  print(max(paint))