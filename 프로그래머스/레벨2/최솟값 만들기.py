# 프로그래머스: 레벨2 최솟값 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0

    A.sort()
    B = sorted(B, reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer

inputA = [1, 4, 2]
inputB = [5, 4, 4]
# expect: 29
print(solution(inputA, inputB))
