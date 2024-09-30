# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 프로그래머스: 등굣길(다이나믹프로그래밍)

# ---------------------
# 1차 시도

def solution(m, n, puddles):
    answer = 0
    matrix = [[True] * m for _ in range(n)]
    for p in puddles:
        y, x = p[0], [1]
        matrix[y - 1][x - 1] = False

    print(match)

    return answer


print(solution(4, 3, [[2,2]]))