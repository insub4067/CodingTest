# 프로그래머스 레벨2: N개의 최소공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/12953

import math

def solution(arr):
    def lcm(a, b):
        return a * b // math.gcd(a, b)

    answer = arr[0]
    
    for num in arr[1:]:
        print(answer, num)
        answer = lcm(answer, num)
    
    return answer

input = [2,6,8,14]	
# expect: 168
print(solution(input))