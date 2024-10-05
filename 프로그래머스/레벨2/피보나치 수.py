# 프로그래머스 레벨2: 피보나치 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    l, r = 0, 1
    for _ in range(n):
        l, r = r, l + r
    return l % 1234567

# except: 2
print(solution(3))