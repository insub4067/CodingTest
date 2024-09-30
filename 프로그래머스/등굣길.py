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
    for x, y in puddles: 
        matrix[y - 1][x - 1] = -1

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

print(solution(4, 3, [[2, 2]]))

# ---------------------
# 2차 시도
# 사용 알고리즘: DP
# 채점 결과
# 정확성: 50.0
# 효율성: 50.0
# 합계: 100.0 / 100.0

def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # 시작점
    
    # 웅덩이 위치 설정
    puddle_set = {(y, x) for x, y in puddles}  
    
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            # 시작점 검사
            if (y, x) == (1, 1):
                continue  
            # 웅덩이 검사
            if (y, x) in puddle_set:
                dp[y][x] = 0  
            # 위쪽과 왼쪽에서 오는 경로의 수 합산
            else:
                dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % MOD  
    
    return dp[n][m]
