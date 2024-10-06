# 레벨2: 괄호 회전하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76502

# ------------- 1차 시도 -------------
# 채점 결과
# 정확성: 85.7
# 합계: 85.7 / 100.0

def solution(s):
    answer = 0

    def check(ss):
        stack = []
        for char in new:
            if char == "}":
                if "{" not in stack:
                    return 0
                else:
                    stack.remove("{")
            if char == ")":
                if "(" not in stack:
                    return 0
                else:
                    stack.remove("(")
            if char == "]":
                if "[" not in stack:
                    return 0
                else:
                    stack.remove("[")
            if char in ["{", "[", "("]:
                stack.append(char)
        if not stack:
            return 1

    for i in range(len(s)):
        left = s[i:]
        right = s[:i]
        new = left + right
        answer += check(new)
    return answer

# ------------- 2차 시도 -------------
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(s):
    answer = 0

    def check(ss):
        stack = []
        for char in ss:
            if char == "}":
                if not stack or stack[-1] != "{":
                    return 0
                stack.pop()
            elif char == ")":
                if not stack or stack[-1] != "(":
                    return 0
                stack.pop()
            elif char == "]":
                if not stack or stack[-1] != "[":
                    return 0
                stack.pop()
            else:
                if char in ["{", "[", "("]:
                    stack.append(char)
        return 1 if not stack else 0
    
    for i in range(len(s)):
        rotated_s = s[i:] + s[:i]
        answer += check(rotated_s)

    return answer

# expect: 3
print(solution("[](){}"))
