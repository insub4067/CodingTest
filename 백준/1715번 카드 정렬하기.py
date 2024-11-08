# 1715번 카드 정렬하기

import heapq

items = []
for i in range(int(input())):
    heapq.heappush(items, int(input()))
    
answer = 0

while len(items) > 1:
    l = heapq.heappop(items)
    r = heapq.heappop(items)
    answer += l + r
    heapq.heappush(items, l + r)

print(answer)
