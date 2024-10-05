# 프로그래머스 레벨2: 짝지어 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char: 
            stack.pop()
        else:
            stack.append(char)  
    
    return 1 if not stack else 0

# except: 1
print(solution("baabaa"))
