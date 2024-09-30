# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 프로그래머스: 등굣길(다이나믹프로그래밍)

# ---------------------
# 1차 시도 - 시간 초과
# 사용 알고리즘: BFS
# 채점 결과
# 정확성: 40.0
# 효율성: 0.0
# 합계: 40.0 / 100.0

from collections import deque

direction = [(0, 1), (1, 0)] # 우, 하
def solution(m, n, puddles):
    matrix = [[0] * m for _ in range(n)]
    totals = []

    # 학교 위치
    matrix[n - 1][m - 1] = 1 
    # 웅덩이 위치 
    for p in puddles: 
        x, y = p[0] - 1, p[1] - 1
        matrix[y][x] = -1

    q = deque()
    q.append((0, 0, 0))
    while q:
        y, x, step = q.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if matrix[ny][nx] == 0:
                    q.append((ny, nx, step + 1))
                if matrix[ny][nx] == 1:
                    totals.append(step + 1)

    minimum = min(totals)
    answer = totals.count(minimum)

    return answer % 1000000007

# ---------------------
# 2차 시도
# 사용 알고리즘: DP
# 채점 결과
# 정확성: 50.0
# 효율성: 50.0
# 합계: 100.0 / 100.0

def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)] # dp 테이블 초기화
    dp[1][1] = 1

    # 웅덩이
    for x, y in puddles:
        dp[y][x] = -1

    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if dp[y][x] == -1: 
                dp[y][x] = 0 
                continue 
            up = dp[y - 1][x]
            left = dp[y][x - 1]
            dp[y][x] += (up + left) % 1000000007
            
    return(dp[n][m])

print(solution(4, 3, [[2, 2]]))