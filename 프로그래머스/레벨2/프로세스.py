# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    answer = 0
    
    # (인덱스넘버, 우선순위)
    t_priorities = []
    
    # 인덱스, 우선순위
    for i, p in enumerate(priorities):
        # (우선순위, 인덱스넘버)
        t_p = (i, p)
        t_priorities.append(t_p)
        
    priorities.sort()
    
    dq = deque(t_priorities)
    while dq:
        i, p = dq.popleft()
        top_p = priorities[len(priorities) - 1]
        if top_p > p:
            dq.append((i, p))
            continue
        else:
            priorities.pop()
            answer += 1
        
        if i == location:
            return answer