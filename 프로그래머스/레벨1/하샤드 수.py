# 하샤드 수

def solution(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return x % sum == 0