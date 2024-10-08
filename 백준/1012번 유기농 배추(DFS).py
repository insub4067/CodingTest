# 1012번 유기농 배추
# https://www.acmicpc.net/problem/1012

from collections import deque

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def solution():
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1  

    visited = [[False] * M for _ in range(N)]
    answer = 0
    
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1 and not visited[y][x]:
                answer += 1
                visited[y][x] = True    
                q = deque([(y, x)])
                
                while q:
                    cy, cx = q.popleft()
                    for dy, dx in directions:
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < N and 0 <= nx < M:
                            if matrix[ny][nx] == 1 and not visited[ny][nx]:
                                visited[ny][nx] = True
                                q.append((ny, nx))
    
    print(answer)

T = int(input())
for _ in range(T):
    solution()