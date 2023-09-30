from collections import deque
n = int(input())
m = int(input())

graph = [[]*n for _ in range(n)]
visited = [0] * n
for _ in range(m):
  a, b = map(int, input().split())
  graph[a-1].append(b-1) 
  graph[b-1].append(a-1)
  
q = deque([0])
visited[0] = 1
while q:
  v = q.popleft()
  for i in graph[v]:
    if visited[i] == 0:
      q.append(i)
      visited[i] = 1

print(sum(visited)-1)
  
# n = int(input())
# m = int(input())
# graph = [[]*n for _ in range(n)]
# for _ in range(m):
#     a,b = map(int,input().split())
#     graph[a-1].append(b-1)
#     graph[b-1].append(a-1)

# cnt = 0
# visited = [0]*(n)
# def dfs(start):
#     global cnt
#     visited[start] = 1
#     for i in graph[start]:
#         if visited[i]==0:
#             dfs(i)
#             cnt +=1
 
# dfs(0)
# print(cnt)