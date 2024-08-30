// 백준 : 1697번 숨바꼭질
// https://www.acmicpc.net/problem/1697

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
max = 100001
visited = [0] * max

def bfs(n):
    q = deque([n])
    while q:
        n = q.popleft()
        if n == k:
            return visited[n]
        for next in (n - 1, n + 1, n * 2):
            if 0 <= next < max and not visited[next]:
                visited[next] = visited[n] + 1
                q.append(next)
                
print(bfs(n))