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

        if visited[ny][nx]:
            continue
        # 범위안이고, 방문하지 않았고, 장애물이 없다면 다음으로 진행
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx] == 1:
            dfs(nx, ny, count + 1)
            
dfs(0, 0, 1)
