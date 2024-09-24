# https://www.acmicpc.net/problem/1149

# 입력
N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

# 테이블 초기화
dp = [[0] * 3 for _ in range(N)]

# 처음 집 비용 할당
dp[0][0] = costs[0][0]  # 빨강
dp[0][1] = costs[0][1]  # 초록
dp[0][2] = costs[0][2]  # 파랑

# 처음 집을 제외한 나머지집에 대한 비용 확인
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0] # 빨강
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1] # 초록
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2] # 파랑

# 마지막 집에 대한 최소 비용 출력
answer = min(dp[N-1])
print(answer)
