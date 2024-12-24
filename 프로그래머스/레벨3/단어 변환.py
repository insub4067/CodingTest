def compare(left, right):
    l = len(left)
    count = 0 
    for i in range(l):
        lc = left[i]
        rc = right[i]
        if lc == rc:
            count += 1
    if count == l - 1:
        return True
    else:
        return False

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    answer = 0
    stack = [begin]
    
    while stack:
        current = stack.pop()
        l = len(current)
        
        if current == target:
            return answer
        
        if compare(current, target):
            return answer + 1
        
        for w in words:
            if compare(current, w):
                stack.append(w)
                words.remove(w)
                answer += 1
                break