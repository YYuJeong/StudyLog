n = int(input())

graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  global cnt
  if x < 0 or x >= n or y < 0 or y >= n:
    return
  
  if graph[x][y] == 1:
    cnt += 1
    graph[x][y] = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(nx, ny)

cnt = 0
cnt_arr = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      dfs(i, j)
      cnt_arr.append(cnt)
      cnt = 0
      
cnt_arr.sort()
print(len(cnt_arr))
for i in cnt_arr:
  print(i)
  
# from collections import deque

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# def bfs(graph, a, b):
#   q = deque()
#   q.append((a, b))
#   graph[a][b] = 0
#   cnt = 1
#   while q:
#     x, y = q.popleft()

#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]

#       if nx < 0 or nx >= n or ny < 0 or ny >= n:
#         continue

#       if graph[nx][ny] == 1:
#         graph[nx][ny] = 0
#         cnt += 1
#         q.append((nx, ny))
#   return cnt 
    
# n = int(input())

# graph = []
# for _ in range(n):
#   graph.append(list(map(int, input())))

# cnt_arr = []
# for i in range(n):
#   for j in range(n):
#     if graph[i][j] == 1:
#       cnt_arr.append(bfs(graph, i, j))

# cnt_arr.sort()
# print(len(cnt_arr))
# for i in cnt_arr:
#   print(i)
