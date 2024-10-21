# 체육복

def solution(n, lost, reserve):
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)
    
    for r in _reserve:
        prev, next = r - 1, r + 1
        if prev in _lost:
            _lost.remove(prev)
        elif next in _lost:
            _lost.remove(next)
            
    return n - len(_lost)
