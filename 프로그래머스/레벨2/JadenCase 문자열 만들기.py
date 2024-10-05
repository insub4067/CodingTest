# 프로그래머스 레벨2: JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    space = False
    
    for i, char in enumerate(s):
        if char == ' ':
            answer += ' '
            space = True
        elif space or i == 0:
            answer += char.upper()
            space = False
        else:
            answer += char.lower()
    
    return answer


input = "3people unFollowed me"
# except: "3people Unfollowed Me"
print(solution(input))
