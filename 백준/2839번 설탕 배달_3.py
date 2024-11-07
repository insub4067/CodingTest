# https://www.acmicpc.net/problem/2839
# 2839번: 설탕 배달

N = int(input())
answer = 0

while N > 0 :
    if N < 3:
        print(-1)
        break

    if N % 5 == 0:
        answer += N // 5
        print(answer)
        break
    
    N -= 3
    answer += 1
    
    if N == 0:
        print(answer)
        break

