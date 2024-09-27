# https://school.programmers.co.kr/learn/courses/30/lessons/178870?language=python3
# 채점 결과
# 정확성: 47.1
# 합계: 47.1 / 100.0

def solution(sequence, k):
    answer = []
    for i in range(len(sequence)):
        temp_sum = 0  
        for ii in range(i, len(sequence)):
            ee = sequence[ii]
            temp_sum += ee  
            if temp_sum > k:
                break
            if temp_sum == k: 
                if not answer or (answer[1] - answer[0]) > (ii - i):
                    answer = [i, ii]
    return answer