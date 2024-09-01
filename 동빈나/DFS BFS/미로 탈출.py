# 미로 탈출.py (DFS)

# 나의 풀이
n, m = 5, 6
graph = [[1,0,1,0,1,0], [1,1,1,1,1,1], [0,0,0,0,0,1], [1,1,1,1,1,1], [1,1,1,1,1,1]]

result = 1
execute = True

def dfs(x, y, count):
    if  x == m - 1 and y == n - 1:
        print(count)
    if 0 <= x < m - 1:
        if graph[y][x + 1] == 1:
            dfs(x + 1, y, count + 1)
    if 0 <= y < n - 1:
        if graph[y + 1][x] == 1:
            dfs(x, y + 1, count + 1)
            
dfs(0, 0, 1)
