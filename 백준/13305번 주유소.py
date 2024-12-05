# 주유소
# https://www.acmicpc.net/problem/13305

N = 4
distances = [2, 3, 1, 0]
prices = [5, 2, 4, 1]

current_price = 0
answer = 0 

for i in range(len(prices)):
    p = prices[i]
    d = distances[i]
    if i == 0 or p < current_price:
        current_price = p
    
    answer += d * current_price

print(answer)