// 모험가 길드

input = "2 3 1 2 2"

n = 5
members = list(map(int, input.split()))
members.sort()

answer = 0 
count = 0

for m in members:
    count += 1
    if count == m:
        answer += 1
        count = 0

print(answer)