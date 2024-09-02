
# 게임 맵 최단거리.py
from collections import deque
ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 통과
def solution(maps):
    
    n, m = len(maps), len(maps[0])
    distances = [[-1] * m for _ in range(n)]
    distances[0][0] = 1
    queue = deque([(0, 0, 1)])
        
    while queue:
        y, x, dist = queue.popleft()
        
        if y == n - 1 and x == m - 1:
            return dist
        
        for dy, dx in ds:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                if distances[ny][nx] == -1:
                    distances[ny][nx] = dist + 1
                    queue.append((ny, nx, dist + 1))
                    
    return -1   

## 통과 But 효율성 통과 X
def solution(maps):
    
    queue = deque([(0, 0, 1)])
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    while queue:
        y, x, dist = queue.popleft()
        
        if y == n - 1 and x == m - 1:
            return dist
        
        for dy, dx in ds:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and maps[ny][nx] == 1:
                    visited[y][x] = True
                    queue.append((ny, nx, dist + 1))
    
    return -1  