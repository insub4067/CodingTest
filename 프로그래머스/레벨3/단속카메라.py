# 프로그래머스: 레벨3 단속카메라
# https://school.programmers.co.kr/learn/courses/30/lessons/42884

# ------------------------
# 1차 시도

def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = -30001
    answer = 0
    
    for route in routes:
        if route[0] > camera:
            answer += 1
            camera = route[1]
    return answer

# expect: 2
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))