// https://www.acmicpc.net/problem/11375
// 백준 : 11375번 열혈강호

import sys

sys.setrecursionlimit(100000)

n, m = map(int,input().split())
tasks = [list(map(int,input().split()))[1:] for _ in range(n)]

matching= [None] * (m + 1)

def dfs(x):
    for task in tasks[x]:
        if not visited[task]:
            visited[task] = True
            inCharge = matching[task]
            if inCharge is None or dfs(inCharge):
                matching[task] = x
                return True                
    return False

result = 0

for i in range(n):
  visited = [False] * (m+1)
  if dfs(i):
    result += 1
  
print(result)
