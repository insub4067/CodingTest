# 프로그래머스: 레벨3 가장 긴 팰린드롬
# https://school.programmers.co.kr/learn/courses/30/lessons/12904

# ---------------------------
# 1차 시도
# 채점 결과
# 정확성: 51.1
# 효율성: 0.0
# 합계: 51.1 / 100.0

def solution(s):
    answer = 0
    length = len(s)

    def compare(i, offset):
        next = offset + 1
        if (i - next) in range(len(s)) and (i + next) in range(len(s)):
            pre = s[i - next]
            follow = s[i + next]
            if pre == follow:
                return compare(i, next)
            else:
                return offset
        else:
            return offset
    
    for i in range(len(s)):
        result = compare(i, 0) * 2 
        answer = max(answer, result + 1)

    return answer

# ---------------------------
# 2차 시도
# 채점 결과
# 정확성: 72.1
# 효율성: 27.9
# 합계: 100.0 / 100.0

def solution(s):

    answer = 0

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                answer = max(answer, j - i)
    
    return answer

# expect: 7
print(solution("abcdcba"))