# https://school.programmers.co.kr/learn/courses/30/lessons/178870?language=python3

# ------------------------------------
# 1번째 시도 (시간 초과)
# 알고리즘: 브루트 포스 O(n^2)
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

# ------------------------------------
# 2번째 시도(통과)
# 알고리즘: 슬라이등 윈도우 O(n)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(sequence, k):
    start = 0
    current_sum = 0
    answer = []
    
    for end in range(len(sequence)):
        current_sum += sequence[end] 

        while current_sum > k and start <= end:
            current_sum -= sequence[start]
            start += 1
        
        if current_sum == k:
            if not answer or (end - start) < (answer[1] - answer[0]):
                answer = [start, end]
    
    return answer