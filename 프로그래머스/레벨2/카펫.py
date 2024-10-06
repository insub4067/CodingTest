# 프로그래머스 레벨2: 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    a = 0 
    while True:
        a += 1
        b = int((brown + yellow) / a)
        if a > 2 and b > 2:
            if (b * 2) + (a * 2) - 4 == brown:
                if b >= a:
                    if (a - 2) * (b - 2) == yellow:
                        answer.append(b)
                        answer.append(a)
                        break
    return answer

# expect: [8, 6]
print(solution(24, 24))