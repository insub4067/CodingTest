# 프로그래머스 레벨2: 귤 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import defaultdict

def solution(k, tangerine):
    dict = defaultdict(int)
    for t in tangerine:
        dict[t] += 1
    counts = sorted(dict.values(), reverse=True)

    answer = 0
    total = 0

    for c in counts:
        total += c
        answer += 1
        if total >= k:
            return answer

inputA = 6
inputB = [1, 3, 2, 5, 4, 5, 2, 3]	
# expect: 3
print(solution(inputA, inputB))
