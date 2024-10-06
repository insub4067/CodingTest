# 레벨2: 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    
    n = len(numbers)
    answer = 0
    
    def dfs(i, num):
        nonlocal answer
        if i == n:
            if num == target:
                answer += 1
            return
        

        dfs(i + 1, num + numbers[i])
        dfs(i + 1, num - numbers[i])
    
    dfs(0, 0)
    return answer