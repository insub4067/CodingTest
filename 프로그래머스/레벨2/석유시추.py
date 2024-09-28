# https://school.programmers.co.kr/learn/courses/30/lessons/250136?language=python3

# ---------------------------------
# 1차 시도
# 알고리즘: BFS
# 정확성: 60.0
# 효율성: 0.0
# 합계: 60.0 / 100.0

from collections import deque
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def solution(land):
    answer = 0
    
    height = len(land)
    width = len(land[0])
    
    def findSize(y, x, land):

        visited[y][x] = True
        answer = 1

        q = deque([(y, x)])
        while q:
            y, x = q.popleft()

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                # 범위 확인
                if 0 <= ny < height and 0 <= nx < width:
                    # 방문, 조건 확인
                    if land[ny][nx] == 1 and not visited[ny][nx]:
                        answer += 1
                        visited[ny][nx] = True
                        q.append((ny, nx))

        return answer 
    
    for x in range(width):
        sum = 0
        visited = [[False] * width for _ in range(height)]
        for y in range(height):
            if land[y][x] == 1 and not visited[y][x]:
                size = findSize(y, x, land)
                sum += size
        answer = max(sum, answer)
    
    return answer

# ---------------------------------
# 2차 시도

from collections import deque
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def solution(land):

    n = len(land)
    m = len(land[0])
    visited = [[False] * m for _ in range(n)]
    totals = [0] * m

    def bfs(y, x):
        count = 1
        visited[y][x] = True
        q = deque([(y, x)])
        xs = {x}

        while q:
            cy, cx = q.popleft()
            for dy, dx in directions:
                ny, nx = dy + cy, dx + cx
                if 0 <= ny < n and 0 <= nx < m:
                    if land[ny][nx] == 1 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((ny, nx))
                        count += 1
                        xs.add(nx)

        for x in xs:
            totals[x] += count
            print(y, x, count)

    for y in range(n):
        for x in range(m):
            if land[y][x] == 1 and not visited[y][x]:
                bfs(y, x)
    
    return max(totals)

input = [
    [0, 0, 0, 1, 1, 1, 0, 0], 
    [0, 0, 0, 0, 1, 1, 0, 0], 
    [1, 1, 0, 0, 0, 1, 1, 0], 
    [1, 1, 1, 0, 0, 0, 0, 0], 
    [1, 1, 1, 0, 0, 0, 1, 1]
]
print(solution(input))