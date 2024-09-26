# 4949번 균형잡힌 세상.py
# https://www.acmicpc.net/problem/4949

while True:
    line = input()  
    if line == ".": 
        break
    
    stack = []
    balanced = True
    
    for char in line:
        if char in ["(", "["]:
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                balanced = False
                break
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                balanced = False
                break
    
    if balanced and not stack:
        print("yes")
    else:
        print("no")