# 프로그래머스 레벨2: 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = []
    stage = 0
    zeros = 0

    while True:
        stage += 1
        zeros += s.count("0")
        s = s.replace("0", "")
        if s == "1":
            break
        s = bin(len(s))[2:]

    answer.append(stage)
    answer.append(zeros)

    return answer

input = "110010101001"
# except: [3,8]
print(solution(input))