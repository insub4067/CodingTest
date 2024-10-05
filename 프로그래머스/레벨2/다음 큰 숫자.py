# 프로그래머스 레벨2: 다음 큰 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    next = n + 1

    while True:
        if bin(n)[2:].count("1") == bin(next)[2:].count("1"):
            return next
        else:
            next += 1

# expect: 83
print(solution(78))