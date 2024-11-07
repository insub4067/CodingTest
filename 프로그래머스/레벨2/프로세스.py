def findShortestPath(startIndex, target, alphas):
    i = alphas.index(target)
    total_l = len(alphas)
    forward = abs(i - startIndex)
    backward = total_l - forward 
    return min(forward, backward)

def solution(name):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = 0
    cursor = 0
    next = 0

    for e in name:
        if e != "A":
            alphaMove = findShortestPath(0, e, alphabets)  
            answer += alphaMove

    for i, e in enumerate(name):
        if e != "A":
            next = i
            break

    answer += findShortestPath(cursor, next, range(len(name)))
    cursor = next

    for c in name[next + 1:]:
        if c != "A":
            answer += 1  
            cursor += 1
        else:
            answer += findShortestPath(cursor, next, range(len(name)))
            cursor = next
            
    return answer


# def solution(name):
#     name = list(map(str, name))
#     alphabets = [
#         "A", "B", "C", "D", "E", 
#         "F", "G", "H", "I", "J", 
#         "K", "L", "M", "N", "O", 
#         "P", "Q", "R", "S", "T", 
#         "U", "V", "W", "X", "Y", "Z"
#     ]
#     total_l = len(alphabets)
    
#     answer = 0
#     current = ["A"] * len(name)
#     cursor = 0

#     for i, e in enumerate(name):
#         if e == "A":
#             continue

#         cursorMove = findShortestPath(cursor, e, name)
#         answer += cursorMove

#         alphaMove = findShortestPath(0, e, alphabets)
#         answer += alphaMove

#         cursor = i
            
#     return answer

result = solution("JAZ")
print(result)