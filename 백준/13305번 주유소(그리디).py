# https://www.acmicpc.net/problem/13305

N = int(input())
distances = list(map(int, input().split()))
distances.append(0)
prices = list(map(int, input().split()))

price = prices[0]
answer = 0 

for i in range(N):
    d = distances[i]
    p = prices[i]
    if price > p:
        price = p
    answer += d * price
    
print(answer)
