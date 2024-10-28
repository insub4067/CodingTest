# 미로 탐색
# https://www.acmicpc.net/problem/2178

from collections import deque

direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
distance = [[0] * M for _ in range(N)]

dq = deque([(0, 0)])
distance[0][0] = 1

while dq:
    cy, cx = dq.popleft()

    if cy == N - 1 and cx == M - 1:
        print(distance[cy][cx])
        break
    
    for dy, dx in direction:
        ny, nx = dy + cy, dx + cx
        if 0 <= ny < N and 0 <= nx < M:
            if graph[ny][nx] == 1 and distance[ny][nx] == 0:
                distance[ny][nx] = distance[cy][cx] + 1
                dq.append((ny, nx))