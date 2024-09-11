# 1715번 카드 정렬하기 (우선순위큐)
import heapq

N = int(input())
cards = [int(input()) for _ in range(N)]
answer = 0

heapq.heapify(cards)

while len(cards) > 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    sum = first + second
    answer += sum 
    heapq.heappush(cards, sum)
            
print(answer)