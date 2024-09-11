# DFS와 BFS
from collections import deque

N, M, V = map(int, input().split())
dfsVisited = [False] * (N + 1)
bfsVisited = [False] * (N + 1)

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    dfsVisited[start] = True
    print(start, end=" ")
    for node in sorted(graph[start]):
        if not dfsVisited[node]:
            dfs(node)
            
def bfs():
    q = deque([V])
    bfsVisited[V] = True
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for node in sorted( graph[cur]):
            if not bfsVisited[node]:
                bfsVisited[node] = True
                q.append(node)
        
dfs(V)
print()
bfs()