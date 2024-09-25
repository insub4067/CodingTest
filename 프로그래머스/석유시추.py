# 석유시추
# https://school.programmers.co.kr/learn/courses/30/lessons/250136?language=python3
# 정확성 - AC
# 효율성 - AF
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