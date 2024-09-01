# 미로 탈출.py (DFS)

# 나의 풀이
n, m = 5, 6
graph = [
    [1,0,1,0,1,0], 
    [1,1,1,1,1,1], 
    [0,0,0,0,0,1], 
    [1,1,1,1,1,1], 
    [1,1,1,1,1,1]
]
visited = [[False] * m for _ in range(n)]

def dfs(x, y, count):
    visited[y][x] = True

    # 도착시 종료
    if  x == m - 1 and y == n - 1:
        print(count)
        return 

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 다음 노드 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 범위 밖이면 통과
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        # 이미 방문했으면 통과
        if visited[ny][nx]:
            continue
        # 장애물이면 통과
        if graph[ny][nx] == 0:
            continue
        dfs(nx, ny, count + 1)
            
dfs(0, 0, 1)