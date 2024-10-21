# 예산

def solution(d, budget):
    answer = 0
    d.sort()

    for i in d:
        if budget - i >= 0:
            budget -= i
            answer += 1
            
    return answer

print(solution([2,2,3,3], 10))