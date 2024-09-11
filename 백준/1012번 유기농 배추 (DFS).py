# 1012번 유기농 배추 (DFS)
T = int(input())  
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

for _ in range(T):
    
    M, N, K = map(int, input().split())
    
    graph = [[0] * M for _ in range(N)] 
    visited = [[False] * M for _ in range(N)]  
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    answer = 0 
    
    for _ in range(K):
        x, y = map(int, input().split()) 
        graph[y][x] = 1 
    
    def dfs(x, y):
        stack = [(x, y)]
        visited[y][x] = True
        while stack:
            cx, cy = stack.pop()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < M and 0 <= ny < N:  
                    if not visited[ny][nx] and graph[ny][nx] == 1:
                        visited[ny][nx] = True
                        stack.append((nx, ny))

    for y in range(N):
        for x in range(M):
            if not visited[y][x] and graph[y][x] == 1: 
                dfs(x, y)  
                answer += 1 

    print(answer) 