# 프로그래머스 레벨2: 점프와 순간 이동
# https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    battery = 0
    
    while n > 0:
        if n % 2 == 0: 
            n //= 2
        else:  
            n -= 1
            battery += 1
    
    return battery

print(solution(5000))