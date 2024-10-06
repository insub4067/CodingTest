# 프로그래머스 레벨2: 멀리 뛰기
# https://school.programmers.co.kr/learn/courses/30/lessons/12914

# 1차 시도 (BFS)
# 채점 결과
# 정확성: 31.3
# 합계: 31.3 / 100.0
from collections import deque

def solution(n):
    answer = 0
    q = deque([n])
    while q:
        v = q.popleft()
        if v == 0:
            answer += 1
            continue
        if v - 1 >= 0:
            q.append(v - 1)
        if v - 2 >= 0:
            q.append(v - 2)
    return answer % 1234567

# 2차 시도 (DP)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0
def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1  
    dp[1] = 1  
    
    for i in range(2, n + 1):
        print(i, dp[i - 1], dp[i - 2])
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n] % 1234567

# expect: 5
print(solution(4))