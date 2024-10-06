# 프로그래머스 레벨2: 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    people.sort()
    left, right = 0, len(people) - 1

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  
        right -= 1
        answer += 1  

    return answer


inputA = [70, 50, 80, 50]	
inputB = 100
# expect: 3
print(solution(inputA, inputB))