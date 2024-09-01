# 음료수 얼려 먹기.py (DFS)

n, m = 4, 5
graph = [[0,0,1,1,0], [0,0,0,1,1], [1,1,1,1,1], [0,0,0,0,0]]

result = 0

def dfs(x, y):
    # 벗어나면 False
    if x < 0 or n <= x or y < 0 or m <= y:
        return False
    # 연결된 노드들 전부 방문 처리
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            
print(result)