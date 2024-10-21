# 정수 제곱근 판별

def solution(n):
    
    cnt = 0
    limit = 50000000000000
    
    while cnt < limit:
        cnt += 1
        squared = cnt ** 2
        if squared == n:
            return  (cnt + 1) ** 2
        elif squared > n:
            return -1