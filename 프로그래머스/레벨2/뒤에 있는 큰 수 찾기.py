# https://school.programmers.co.kr/learn/courses/30/lessons/154539

# ---------------------
# 1차 시도: 시간 초과
# 알고리즘: '브루트 포스' O(n^2)
# 채점 결과
# 정확성: 82.6
# 합계: 82.6 / 100.0

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        bigger_num = -1
        for ii in range(i, len(numbers)):
            if numbers[ii] > numbers[i]:
                bigger_num = numbers[ii]
                break
        answer.append(bigger_num)
    return answer

# ---------------------
# 2차 시도: 통과
# 알고리즘: 'Next Greater Element' O(n)

def solution(numbers):
    answer = [-1] * len(numbers) 
    stack = []  

    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            idx = stack.pop()
            answer[idx] = num
        stack.append(i)  

    return answer

print(solution([2, 3, 3, 5])) # expect: [3, 5, 5, -1]