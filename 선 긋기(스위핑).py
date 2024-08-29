// 백준 : 2170번 선 긋기(스위핑)
// https://www.acmicpc.net/problem/2170

import sys
input = sys.stdin.readline

n = int(input())

locations = [tuple(map(int, input().split())) for _ in range(n)]
result = 0

locations.sort()
start, end = locations[0]

for location in locations:
    x, y = location
    if end >= x:
        end = max(y, end)
    else:
        result += (end - start)
        start, end = x, y
      
result += (end - start)
print(result)