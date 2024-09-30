# 프로그래머스 레벨3: 여행경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164

# ----------------------------
# 1차 시도 
# 사용 알고리즘: BFS
# 채점 결과
# 정확성: 50.0
# 합계: 50.0 / 100.0

from collections import deque

def solution(tickets):
    tickets = sorted(tickets, key=lambda t: t[1])
    visited = [False] * len(tickets)
    answer = []
    q = deque()

    for i, e in enumerate(tickets):
        if e[0] == "ICN":
            q.append(e)
            visited[i] = True
            break

    while q:
        leave, arrival = q.popleft()
        answer.append(leave)

        if visited.count(False) == 0:
            answer.append(arrival)
            break

        for i, e in enumerate(tickets):
            if e[0] == arrival and not visited[i]:
                q.append(e)
                visited[i] = True
                break

    return answer

# ----------------------------
# 2차 시도 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0
from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for start, end in tickets:
        routes[start].append(end)

    for k in routes.keys():
        routes[k].sort(reverse=True)

    stack = ["ICN"]
    while stack:
        top = stack[-1]
        if top not in routes or not routes[top]:
            answer.append(stack.pop())   
        else:
            stack.append(routes[top].pop())

    return answer[::-1]

# expect ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])) 